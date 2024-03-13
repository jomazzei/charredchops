from django.http import HttpResponseForbidden
from allauth.account.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Reservation


# Create your views here.
def booking(request):
    """
    Renders the booking page
    """
    return render(request, "booking/booking.html")

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
