import random
import string
from datetime import time, date
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.utils.text import slugify


# Create your models here.
class Reservation(models.Model):
    """
    Stores the data for a single instance of a reservation
    """

    TIME_SLOTS = (
        (time(17, 0), "5:00 PM"),
        (time(17, 30), "5:30 PM"),
        (time(18, 0), "6:00 PM"),
        (time(18, 30), "6:30 PM"),
        (time(19, 0), "7:00 PM"),
        (time(19, 30), "7:30 PM"),
        (time(20, 0), "8:00 PM"),
        (time(20, 30), "8:30 PM"),
        (time(21, 0), "9:00 PM"),
        (time(21, 30), "9:30 PM"),
        (time(22, 0), "10:00 PM"),
    )

    entry_id = models.AutoField(primary_key=True, unique=True)
    cust_ref = models.CharField(blank=True, unique=True, max_length=8)

    slug = models.SlugField(max_length=250, blank=True, null=False, unique=True)

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking", null=False
    )
    cust_fname = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[RegexValidator("[a-zA-Z]")],
    )
    cust_lname = models.CharField(
        max_length=20,
        blank=False, null=False,
        validators=[RegexValidator("[a-zA-Z]")]
    )
    email = models.EmailField()
    guest_count = models.IntegerField(
        blank=False,
        null=False,
        default=1,
        validators=[MaxValueValidator(8), MinValueValidator(1)],
    )
    booking_date = models.DateField(
        null=False,
        blank=False,
        validators=[MinValueValidator(limit_value=date.today())],
    )
    booking_time = models.TimeField(null=False, blank=False, choices=TIME_SLOTS)
    comments = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["booking_date", "booking_time", "guest_count", "entry_id"]

    def __str__(self):
        return f"Date: {self.booking_date} | ID: {self.entry_id} | Reference: {self.cust_ref}"

    # Queried ChatGPT on how to create unique references
    # that do not extend beyond a comprehendable digit count

    # 2 Stage approach for generating customer references.
    # First, generate a random alphanumeric string of 6 digits
    # and check it against previous reference entries.
    # If previous entry CONTAINS (important,
    # as straight equal check wouldn't account for stage 2) the random id, re run until pass.

    # Second, after a new unique string is generated,
    # get customer initials and append them to the front of the string.
    # Return the new formatted id and call the entire process in the save method.
    def generate_unique_booking_id(self):
        """
        Generates unique alphanumeric string.

        Checks if previous cust_ref entries contain new string,
        if passes, returns the string value of random_id
        """
        is_unique = False
        while not is_unique:
            random_id = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=6)
            )
            # Must be Reservation.objects, not self.objects, as otherwise admin error is thrown
            if not Reservation.objects.filter(cust_ref__icontains=random_id).exists():
                is_unique = True
                return random_id

    def format_booking_id(self):
        """
        Calls generate_unique_booking_id function to get a random string.
        Customer intials appended to front of the new string.
        This new string is then returned.
        """
        random_ref = self.generate_unique_booking_id()
        intials = f"{self.cust_fname[0]}{self.cust_lname[0]}"

        formatted_reference = f"{intials}{random_ref}"

        self.cust_ref = formatted_reference

        return formatted_reference

    def save(self, *args, **kwargs):
        # Call the format_entry_id method to generate and set the booking ID
        self.format_booking_id()

        # Automatically generates slug for url based on cust_ref field
        if not self.slug:
            self.slug = slugify(self.cust_ref)

        super().save(*args, **kwargs)
