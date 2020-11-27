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