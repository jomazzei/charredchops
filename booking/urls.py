from django.urls import path
from . import views

urlpatterns = [
    path("booknow/", views.booking, name="bookingpage"),
    path("mybookings/", views.manage_booking_cust, name="custlist"),
    
    path("mybookings/<slug:slug>/", views.booking_details, name="bookingdetails"),
]
