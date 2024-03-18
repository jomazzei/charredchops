from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from allauth.account.decorators import login_required
from .models import Reservation
from .forms import BookTableForm, UpdateBookingForm


# Create your views here.
def booking(request):
    """
    Renders the booking page.
    
    Also renders the booking form
    and controls the validation, saving, and posting.
    """    
    if request.method == "POST":
        booking_form = BookTableForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                "You have successfully booked a reservation!"
            )
            return redirect("success/")

        # If form is NOT valid
        else:
            messages.add_message(
                request, messages.ERROR,
                "Please check your form answers"
            )

        # Handles refresh to cancel form resubmission
        return HttpResponseRedirect(request.path_info)

    else:
        booking_form = BookTableForm()

    return render(
        request,
        "booking/booking.html",
        {
            "booking_form": booking_form
        })


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
    context_object_name = 'booking_list'

    # queryset = Reservation.objects.all()
    template_name = "booking/booking_list.html"

    # Filter to only owned bookings
    def get_queryset(self):
        return Reservation.objects.filter(customer=self.request.user).order_by("-booking_date")


@login_required
def booking_details(request, slug):
    """
    Renders the details of a single reservation item
    Customer can view details here
    """
    queryset = Reservation.objects.all()
    reservation = get_object_or_404(queryset, slug=slug)

    # Checks for owner of reservation item vs. the user visiting url
    if request.user == reservation.customer:
        return render(request, "booking/booking_details.html",
                  {
                      "reservation": reservation,
                  })

    else:
        raise PermissionDenied()


@login_required
def booking_update(request, slug):
    """
    Renders the update page.
    Customer can edit their details here
    """
    queryset = Reservation.objects.all()
    reservation = get_object_or_404(queryset, slug=slug)
    updating_form = UpdateBookingForm(instance=reservation)

    if request.method == "POST" and request.user == reservation.customer:
        update_form = UpdateBookingForm(request.POST, instance=reservation)

        if update_form.is_valid():
            booking = update_form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                "You have successfully updated your reservation"
            )
            return redirect(
                reverse('bookingdetails',
                        kwargs={'slug': reservation.slug})
                )

        # If form is NOT valid
        else:
            messages.add_message(
                request, messages.ERROR,
                "Please check your form answers"
            )

    elif request.user == reservation.customer:
        return render(request, "booking/form_update_booking.html",
                  {
                      "reservation": reservation,
                      "update_form": updating_form
                  })

    else:
        raise PermissionDenied()
