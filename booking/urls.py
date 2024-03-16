from django.urls import path
from . import views

urlpatterns = [
    # Booking contact/form page
    path("booknow/", views.booking, name="bookingpage"),
    # Form success redirect page
    path("booknow/success/", views.booking_success, name="bookingsuccess"),
    
    # Bookings list
    path("mybookings/", views.BookingList.as_view(), name="bookinglist"),
    # Single reservation/booking
    path("mybookings/<slug:slug>/", views.booking_details, name="bookingdetails"),
]
