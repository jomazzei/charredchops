from django import forms
from .models import Reservation


class BookTableForm(forms.ModelForm):
    """
    Form to book table
    """
    class Meta:
        model = Reservation
        fields = ("cust_fname","cust_lname",
                  "email","guest_count",
                  "booking_date","booking_time",
                  "comments",
                )
