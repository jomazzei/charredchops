import datetime
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
      labels = {
            "cust_fname": "First name",
            "cust_lname": "Last name",
            "email": "Your email address",
            "booking_date": "What day would you like to book?",
            "booking_time": "What time would you like your reservation to be?",
            "comments": "Special comments, requests, or allergies",
        }
      widgets = {
          'booking_date': forms.DateInput(attrs={'type': 'date',}),
          'booking_time': forms.TimeInput(attrs={'type': 'time',}),
      }
