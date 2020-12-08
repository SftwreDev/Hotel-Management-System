from django.db import models

from accounts.models import User
import datetime

class Room(models.Model):
    room = (
        ('Single Bed Size Room' , 'Single Bed Size Room'),
        ('Double Bed Size Room', 'Double Bed Size Room'),
        ('Family Bed Size Room', 'Family Bed Size Room')
    )
    id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=100, choices=room , verbose_name = 'Type of Room')
    room_no = models.PositiveIntegerField(verbose_name = 'Room No', unique=True, help_text = "Should be unique and not existing room no")
    rates = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = "Rates per Room")
    available = models.BooleanField(default=False, verbose_name="Available")


    def __str__(self):
        return f"{self.room_type}" + " | " + "Room " + f"{self.room_no}"

class Reservations(models.Model):
    room = (
        ('Standard Room' , 'Standard Room'),
        ('Deluxe Room', 'Deluxe Room'),
        ('VIP Room', 'VIP Room')
    )
    customer = models.ForeignKey(User, on_delete = models.CASCADE, related_name="reservation_user" )
    name = models.CharField(max_length = 255, verbose_name = 'Customer Name')
    address = models.CharField(max_length = 255, verbose_name = 'Address')
    email_address = models.EmailField(verbose_name = 'Email Address')
    contact = models.CharField(max_length = 255, verbose_name = 'Contact No')
    type_of_id = models.CharField(max_length = 255, verbose_name = 'Type of ID')
    id_no = models.CharField(max_length = 255, verbose_name = 'ID No')
    no_of_days = models.CharField(max_length = 255, verbose_name = 'No of Days')
    check_in_datetime = models.DateTimeField(auto_now_add=False, verbose_name = "Date & Time for Check In")
    check_out_datetime = models.DateTimeField(auto_now_add=False, verbose_name = "Date & Time for Check Out")
    check_in_datetime = models.DateTimeField(auto_now_add=False, verbose_name = "Date & Time for Check In")
    check_out_datetime = models.DateTimeField(auto_now_add=False, verbose_name = "Date & Time for Check Out")
    # check_in_date = models.DateField(auto_now_add=False, verbose_name = "Date for Check In")
    # check_out_date = models.DateField(auto_now_add=False, verbose_name = "Datefor Check Out")
    # check_in_time = models.TimeField(auto_now_add=False, verbose_name = "Time for Check In")
    # check_out_time = models.TimeField(auto_now_add=False, verbose_name = "Time for Check Out")
    room = models.ForeignKey(Room, on_delete = models.SET_NULL,null=True,related_name="room_type_and_no", verbose_name = "Room Type & No" )
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}"

    def no_of_hrs(self):
        return self.check_in_datetime - self.check_out_datetime



class CheckInAndOut(models.Model):
    reservations = models.ForeignKey(Reservations, on_delete = models.CASCADE, verbose_name = "Customer's Reservations")
    check_in = models.BooleanField(default=False, verbose_name = "Checking In or Out?", help_text="Check if check in , uncheck if check out")
    check_in_date_time = models.DateTimeField(auto_now_add = False)
    def __str__(self):
        return self.reservations.customer