from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from allauth.account.decorators import login_required
from .models import Reservation
from .forms import BookTableForm, UpdateBookingForm


# Create your views here.
def booking_page(request):
    """
    Renders the booking page.

    Also renders the booking form
    and controls the validation, saving, and posting.
    """

    def compare_new_booking(new_date):
        """
        Checks desired updated date against previous entries
        """
        if Reservation.objects.filter(
            customer=request.user, booking_date=new_date
        ).exists():
            messages.add_message(
                request,
                messages.ERROR,
                """You already have a booking for this day, 
                if you would like to change the time or cancel please 
                navigate to the 'My bookings' tab and select the booking you wish 
                to change.""",
            )
            return True

    if request.method == "POST":
        form = BookTableForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user

            # Checks if user has a previous reservation on the date they chose
            chosen_date = booking.booking_date
            if compare_new_booking(chosen_date):
                return render(request, "booking/booking.html", {"form": form})

            # Regular save handling
            else:
                booking.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "You have successfully booked a reservation!",
                )
                return redirect(
                    reverse("booking_details_page", kwargs={"slug": booking.slug})
                )

        # If form is NOT valid
        else:
            messages.add_message(
                request, messages.ERROR, "Please check your form again."
            )
            # Returns the form so template can iterate field errors in template.
            return render(request, "booking/booking.html", {"form": form})
            # Can cause resubmissions on refresh, need to fix

    else:
        form = BookTableForm()

    return render(request, "booking/booking.html", {"form": form})


class BookingList(LoginRequiredMixin, generic.ListView):
    """
    Renders the list view.
    Customer can manage their bookings here
    """

    model = Reservation
    # Found online, won't iterate without this definition, unlike in previous projects
    context_object_name = "booking_list"

    # queryset = Reservation.objects.filter(customer=self.request.user).order_by(
    #         "-booking_date"
    #     )
    template_name = "booking/booking_list.html"

    # Filter to only owned bookings
    def get_queryset(self):
        return Reservation.objects.filter(customer=self.request.user).order_by(
            "-booking_date"
        )


@login_required
def booking_details(request, slug):
    """
    Renders the details of a single reservation item
    Customer can view details here
    """
    queryset = Reservation.objects.all()
    reservation_item = get_object_or_404(queryset, slug=slug)

    # Checks for owner of reservation item vs. the user visiting url
    if request.user == reservation_item.customer:
        return render(
            request,
            "booking/booking_details.html",
            {
                "reservation_item": reservation_item,
            },
        )

    else:
        raise PermissionDenied()


@login_required
def booking_update(request, slug):
    """
    Renders the update page.
    Customer can edit their details here
    """
    queryset = Reservation.objects.all()
    reservation_item = get_object_or_404(queryset, slug=slug)
    form = UpdateBookingForm(instance=reservation_item)

    def compare_bookings_for_update():
        """
        Checks desired updated date against previous entries,
        excluding current reservation's date.
        """
        # 1. Needs to check if desired date matches owned items.
        # 2. Cannot save onto owned items EXCEPT on the same date
        # as the booking currently being edited.

    if request.method == "POST" and request.user == reservation_item.customer:
        form = UpdateBookingForm(request.POST, instance=reservation_item)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user

            booking.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "You have successfully updated your reservation",
            )
            return redirect(
                reverse("booking_details_page", kwargs={"slug": reservation_item.slug})
            )

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "One or more of your inputs were invalid, please re-enter your answers",
            )
            return redirect(request.path_info)

    elif request.user == reservation_item.customer:
        return render(
            request,
            "booking/form_update_booking.html",
            {"reservation_item": reservation_item, "form": form},
        )

    else:
        raise PermissionDenied()


@login_required
def booking_delete(request, slug):
    """
    Handles delete logic
    """
    queryset = Reservation.objects.all()
    reservation_item = get_object_or_404(queryset, slug=slug)

    if request.user == reservation_item.customer:
        reservation_item.delete()
        return redirect(reverse("booking_list_page"))

    else:
        raise PermissionDenied()
