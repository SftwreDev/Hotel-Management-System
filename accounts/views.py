from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from .models import User
from .forms import CustomerSignUpForm, PersonnelSignUpForm, AdministratorSignUpForm

class CustomerSignUp(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('reservations:homepage')



class PersonnelSignUp(CreateView):
    model = User
    form_class = PersonnelSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'personnel'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('reservations:homepage')

class AdminSignUp(CreateView):
    model = User
    form_class = AdministratorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('reservations:homepage')

class SignUpChoices(TemplateView):
    template_name = 'accounts/sign_up_option.html'
