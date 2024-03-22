from django.urls import path
from . import views

urlpatterns = [
    # Booking contact/form page
    path("booknow/", views.booking_page, name="booking_page"),
    # Bookings list
    path("mybookings/", views.BookingList.as_view(), name="booking_list_page"),
    # Booking detail
    path(
        "mybookings/<slug:slug>/",
        views.booking_details,
        name="booking_details_page"
    ),
    path(
        "mybookings/<slug:slug>/update",
        views.booking_update,
        name="booking_update_page",
    ),
    path(
        "mybookings/<slug:slug>/cancel",
        views.booking_delete,
        name="booking_delete_page",
    ),
]
