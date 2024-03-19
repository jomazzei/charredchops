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
    if request.method == "POST":
        form = BookTableForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS, "You have successfully booked a reservation!"
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


def booking_success(request):
    """
    Renders a success page,
    only used in booking form validation feedback
    """
    return render(request, "booking/form_success.html")


class BookingList(LoginRequiredMixin, generic.ListView):
    """
    Renders the list view.
    Customer can manage their bookings here
    """

    model = Reservation
    # Found online, won't iterate without this definition,
    # unlike in the previous projects
    context_object_name = "booking_list"

    # queryset = Reservation.objects.all()
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

        # If form is NOT valid
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
