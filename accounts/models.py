from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_personel = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name = 'customer_user')

    def __str__(self):
        return self.user.email


class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, related_name = 'personnel_user')

    def __str__(self):
        return self.user.email



class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, related_name = 'admin_user')

    def __str__(self):
        return self.user.email


class CustomerInfo(models.Model):
    id_type = (
        ('Philhealth', 'Philhealth'),
        ('TIN ID', 'TIN ID'),
        ("Voter's ID", "Voter's ID"),
        ("Passport", "Passport"),
        ("UMID ID", "UMID ID"),
        ("Driver's License", "Driver's License"),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    l_name = models.CharField(max_length=255, verbose_name="Last Name")
    f_name = models.CharField(max_length=255, verbose_name="First Name")
    address = models.CharField(max_length=255, verbose_name="Address")
    email_add = models.EmailField(verbose_name="Email Address")
    contact_no = models.CharField(max_length=255, verbose_name="Contact No")
    age = models.CharField(max_length = 255, verbose_name="Age")
    type_of_id = models.CharField(max_length=255, choices=id_type, verbose_name='Type of ID')
    id_no = models.CharField(max_length=255, verbose_name="ID No")