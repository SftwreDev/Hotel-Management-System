from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth import login
from .models import User, Customer, Personnel, Administrator
from .forms import CustomerSignUpForm, PersonnelSignUpForm, AdministratorSignUpForm
from django.contrib.auth.decorators import login_required

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
        kwargs['user_type'] = 'personel'
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
        kwargs['user_type'] = 'administrator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('reservations:homepage')

class SignUpChoices(TemplateView):
    template_name = 'accounts/sign_up_option.html'


@login_required
def view_customer_account_list(request):
    template_name = 'accounts/customer_account_list.html'

    customer = User.objects.filter(is_customer = "True")
    print(customer)
    context = { 'customer' : customer }

    return render(request, template_name, context)

@login_required
def delete_customer_account(request, pk):

    obj = User.objects.get(id=pk)
    obj.delete()

    return redirect('accounts:customer_account')

@login_required
def update_customer_account(request, pk):
    template_name = 'accounts/customer_account_update.html'

    customer = get_object_or_404(User, pk=pk)
    form = CustomerSignUpForm(request.POST or None, instance = customer)

    if form.is_valid():
        form.save()
        messages.info(request, "Successfully updated a account")
        return redirect("accounts:customer_account")
    else:
        form = CustomerSignUpForm(request.POST or None, instance = customer)
    
    context = { 'form' : form }

    return render(request, template_name, context)

@login_required
def view_personnel_account_list(request):
    template_name = 'accounts/personnel_account_list.html'

    personnel = User.objects.filter(is_personel = "True")

    context = { 'personnel' : personnel }

    return render(request, template_name, context)

@login_required
def delete_personnel_account(request, pk):

    obj = User.objects.get(id=pk)
    obj.delete()

    return redirect('accounts:personnel_account')

@login_required
def update_personnel_account(request, pk):
    template_name = 'accounts/personnel_account_update.html'

    personnel = get_object_or_404(User, pk=pk)
    form = PersonnelSignUpForm(request.POST or None, instance = personnel)

    if form.is_valid():
        form.save()
        messages.info(request, "Successfully updated a account")
        return redirect("accounts:personnel_account")
    else:
        form = PersonnelSignUpForm(request.POST or None, instance = personnel)
    
    context = { 'form' : form }

    return render(request, template_name, context)

@login_required
def view_admin_account_list(request):
    template_name = 'accounts/admin_account_list.html'

    admin = User.objects.filter(is_administrator = "True")

    context = { 'admin' : admin }

    return render(request, template_name, context)

@login_required
def delete_admin_account(request, pk):

    obj = User.objects.get(id=pk)
    obj.delete()

    return redirect('accounts:admin_account')

@login_required
def update_admin_account(request, pk):
    template_name = 'accounts/admin_account_update.html'

    admin = get_object_or_404(User, pk=pk)
    form = AdministratorSignUpForm(request.POST or None, instance = admin)

    if form.is_valid():
        form.save()
        messages.info(request, "Successfully updated a account")
        return redirect("accounts:admin_account")
    else:
        form = AdministratorSignUpForm(request.POST or None, instance = admin)
    
    context = { 'form' : form }

    return render(request, template_name, context)