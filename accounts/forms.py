from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Customer, Personnel, Administrator


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ['username', 'email' , 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user


class PersonnelSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ['username', 'email' , 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_personnel = True
        user.save()
        return user


class AdministratorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ['username', 'email' , 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        return user