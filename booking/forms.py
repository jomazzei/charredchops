from datetime import timedelta
from django import forms
from django.utils.timezone import now
from .models import Reservation


class BookTableForm(forms.ModelForm):
    """
    Form to book table
    """

    class Meta:
        model = Reservation
        fields = (
            "cust_fname",
            "cust_lname",
            "email",
            "guest_count",
            "booking_date",
            "booking_time",
            "comments",
        )
        labels = {
            "cust_fname": "First name",
            "cust_lname": "Last name",
            "email": "Your email address",
            "guest_count": "How many guests? Up to 8 people",
            "booking_date": "What day would you like to book?",
            "booking_time": "What time slot?",
            "comments": "Special comments, requests, or allergies",
        }
        widgets = {
            "booking_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "min": now().isoformat(),
                    "max": (now() + timedelta(weeks=52)).isoformat(),
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["cust_fname"] = cleaned_data.get("cust_fname", "").strip()
        cleaned_data["cust_lname"] = cleaned_data.get("cust_lname", "").strip()
        cleaned_data["email"] = cleaned_data.get("email", "").strip()
        cleaned_data["comments"] = cleaned_data.get("comments", "").strip()
        return cleaned_data


class UpdateBookingForm(forms.ModelForm):
    """
    Form to book table
    """

    class Meta:
        model = Reservation
        fields = (
            "cust_fname",
            "cust_lname",
            "email",
            "guest_count",
            "booking_date",
            "booking_time",
            "comments",
        )
        labels = {
            "cust_fname": "First name",
            "cust_lname": "Last name",
            "email": "Email",
            "guest_count": "Updated guests, max 8",
            "booking_date": "Updated date",
            "booking_time": "Updated time slot",
            "comments": "Special comments, requests, or allergies",
        }
        widgets = {
            "booking_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["cust_fname"] = cleaned_data.get("cust_fname", "").strip()
        cleaned_data["cust_lname"] = cleaned_data.get("cust_lname", "").strip()
        cleaned_data["email"] = cleaned_data.get("email", "").strip()
        cleaned_data["comments"] = cleaned_data.get("comments", "").strip()
        return cleaned_data
