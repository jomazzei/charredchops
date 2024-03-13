from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from django.utils.text import slugify


# Create your models here.
class Reservation(models.Model):
    """
    Stores the data for a single instance of a reservation
    """
    entry_id = models.AutoField(primary_key=True, unique=True)
    
    booking_id_ux = models.CharField(blank=True, max_length=8)


    customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="booking")
    cust_fname = models.CharField(max_length=20, blank=False)
    cust_lname = models.CharField(max_length=20, blank=False)
    phone_number = PhoneNumberField(blank=False)
    email = models.EmailField(blank=False, null=False)
    guest_count = models.IntegerField(blank=False, null=False)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    comments = models.TextField()
    allergies = models.TextField
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField()
    cancelled = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ["booking_date", "booking_time", "guest_count"]
    
    
    def __str__(self):
        return f"{self.entry_id}"
    
    
    def format_booking_id(self):
        """
        Formats the database entry ID to a more human
        readable way for customer reference
        """
        entry_id_str = str(self.entry_id).zfill(6)
        
        intials = f"{self.cust_fname[0]}{self.cust_lname[0]}"
        
        booking_reference = f"{entry_id_str}{intials}"
        
        self.booking_id_ux = booking_reference
        
        return booking_reference
    
    
    def save(self, *args, **kwargs):
        # Call the format_entry_id method to generate and set the booking ID
        self.format_booking_id()

        # Call the parent class's save method to save the instance
        super().save(*args, **kwargs)