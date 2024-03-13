from django.shortcuts import render


# Create your views here.
def booking(request):
    """
    Renders the booking page
    """
    return render(request, "booking/booking.html")