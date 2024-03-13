from django.urls import path
from . import views

urlpatterns = [
    path("booknow/", views.booking, name="bookingpage"),
]
