from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from allauth.account.decorators import login_required
from .models import Reservation
from .forms import BookTableForm


# Create your views here.
def booking(request):
    """
    Renders the booking page.
    
    Also renders the booking form
    and controls the validation, saving, and posting.
    """
    booking_form = BookTableForm()
    
    if request.method == "POST":
        booking_form = BookTableForm()
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


# Refer to previous projects for list view.
# This is a base url hook to get the link to work
@login_required
def manage_booking_cust(request):
    """
    Renders the list view.
    Customer can manage their bookings here
    """
    return render(request, "booking/cust_list.html")


@login_required
def booking_details(request, slug):
    """
    Renders the details of a single reservation item
    Customer can edit details here
    """
    queryset = Reservation.objects.all()
    reservation = get_object_or_404(queryset, slug=slug)

    if request.user == reservation.customer:
        return render(request, "booking/booking_details.html",
                  {
                      "reservation": reservation
                  })
    else:
        return HttpResponseForbidden
