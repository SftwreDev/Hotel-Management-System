from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Customer, Personnel, Administrator


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email' , 'password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        return user


class PersonnelSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email' , 'password1', 'password2']

    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_personel = True
        if commit:
            user.save()
        return user


class AdministratorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email' , 'password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_administrator = True
        if commit:
            user.save()
        return user