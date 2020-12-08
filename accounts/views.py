from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth import login
from .models import User, Customer, Personnel, Administrator, CustomerInfo
from .forms import CustomerSignUpForm, PersonnelSignUpForm, AdministratorSignUpForm, CustomerInfoForm
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
        return redirect('accounts:customer_info')

class CustomerSignUpPage(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts:customer_account')

class PersonnelSignUp(CreateView):
    model = User
    form_class = PersonnelSignUpForm
    template_name = 'registration/personnel_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'personel'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts:personnel_account')

class AdminSignUp(CreateView):
    model = User
    form_class = AdministratorSignUpForm
    template_name = 'registration/admin_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'administrator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts:admin_account')

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


def customer_info(request):
    template_name = 'accounts/customer_info_form.html'

    form = CustomerInfoForm(request.POST or None)
    
    if form.is_valid():
        cx = form.save(commit=False)
        cx.customer = request.user
        cx.save()
        messages.success(request, "You have successfully completed your registration")
        return redirect('reservations:homepage')
    else:
        form = CustomerInfoForm(request.POST or None)

    context = {
        'form' : form
    }

    return render(request, template_name, context)


def cx_info_list(request):
    template_name = 'accounts/cx_info_list.html'

    cx = CustomerInfo.objects.filter(customer = request.user)

    context = {
        'cx' : cx
    }

    return render(request, template_name, context)


def cx_info_update(request, pk):
    template_name = 'accounts/customer_info_form.html'

    obj = get_object_or_404(CustomerInfo, pk=pk)
    form = CustomerInfoForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        cx = form.save(commit=False)
        cx.customer = request.user
        cx.save()
        messages.success(request, "You have successfully completed your registration")
        return redirect('accounts:cx_info_list')
    else:
        form = CustomerInfoForm(request.POST or None, instance=obj)

    context = {
        'form' : form
    }

    return render(request, template_name, context)


def delete_info(request, pk):

    obj = CustomerInfo.objects.get(id=pk)
    obj.delete()
    return redirect('accounts:cx_info_list')