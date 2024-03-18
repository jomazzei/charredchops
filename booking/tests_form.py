from django.test import TestCase
from .forms import BookTableForm


# Checks if is.valid() = True.
# assertTrue checks if (argument) is true
class TestBookingForm(TestCase):

    def test_form_is_valid(self):

        booking_form = BookTableForm(
            {
                "cust_fname": "Joe",
                "cust_lname": "Mazzei",
                "email": "j.mazzei.pv@gmail.com",
                "booking_date": "04/12/2024",
                "booking_time": "10:00",
                "guest_count": 1,
            }
        )
        if not booking_form.is_valid():
            for field, errors in booking_form.errors.items():
                print(f"Field: {field}")
                for error in errors:
                    print(f"Error: {error}")

        self.assertTrue(booking_form.is_valid(), msg="Form is not valid")
