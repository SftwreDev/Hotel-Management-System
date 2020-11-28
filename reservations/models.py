from django.db import models

from accounts.models import User

class Room(models.Model):
    room = (
        ('Standard Room' , 'Standard Room'),
        ('Deluxe Room', 'Deluxe Room'),
        ('VIP Room', 'VIP Room')
    )
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
    check_in_datetime = models.DateTimeField(auto_now_add=False, verbose_name = "Date & Time for Check In")
    check_out_datetime = models.DateTimeField(auto_now_add=False, verbose_name = "Date & Time for Check Out")
    hrs_to_stay = models.PositiveIntegerField(verbose_name = 'Hours to Stay')
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name="room_type_and_no", verbose_name = "Room Type & No" )
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}"




class CheckInAndOut(models.Model):
    reservations = models.ForeignKey(Reservations, on_delete = models.CASCADE, verbose_name = "Customer's Reservations")
    check_in = models.BooleanField(default=False, verbose_name = "Checking In or Out?", help_text="Check if check in , uncheck if check out")
    check_in_date_time = models.DateTimeField(auto_now_add = False)
    def __str__(self):
        return self.reservations.customer