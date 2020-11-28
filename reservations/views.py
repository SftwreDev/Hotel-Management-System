from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

from accounts.decorators import customer_required, personnel_required, administrator_required
from .forms import ReservationForm, RoomForm,RoomModalForm, CheckInAndOutForm,ReservationFormField
from .models import Reservations, Room, CheckInAndOut
import datetime
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)
from accounts.models import User, Customer, Personnel, Administrator



@login_required
def homepage(request):
    """ This is where we render the homepage og this system """


    template_name = "reservations/home.html"

    context = {}
    
    return render(request, template_name, context)

@login_required
def create_reservations(request):
    """ This is where we render the forms for creating new reservations """
    
    template_name = "reservations/create_reservations.html"

    form = ReservationForm(request.POST or None)
    
    if form.is_valid():
        reserved = form.save(commit=False)
        reserved.customer = request.user
        reserved.save()
        messages.success(request, "You have successfully create a new reservations")
        return redirect('reservations:reservations_list')
    else:
        form = ReservationForm(request.POST or None)

    context = {
        'form' : form
    }

    return render(request, template_name, context)

@login_required
def update_reservations(request, pk):
    """ This is where we render the forms for updating existing reservations """

    template_name = "reservations/update_reservations.html"
    reservation = get_object_or_404(Reservations, pk=pk)
    form = ReservationForm(request.POST or None, instance=reservation)

    if form.is_valid():
        update = form.save(commit=False)
        update.customer = request.user
        update.save()
        messages.success(request, "You have successfully update an existing reservations")
        return redirect('reservations:reservations_list')
    else:
        form = ReservationForm(request.POST or None, instance=reservation)
    
    context = { 'form' : form }
    return render(request, template_name, context)

@login_required
def update_reservations_view(request, pk):
    """ This is where we render the forms for updating existing reservations """

    template_name = "reservations/update_reservations.html"
    reservation = get_object_or_404(Reservations, pk=pk)
    form = ReservationForm(request.POST or None, instance=reservation)

    if form.is_valid():
        update = form.save(commit=False)
        update.customer = reservation.customer
        update.save()
        messages.success(request, "You have successfully update an existing reservations")
        return redirect('reservations:reservations_list_view')
    else:
        form = ReservationForm(request.POST or None, instance=reservation)
    
    context = { 'form' : form }
    return render(request, template_name, context)

@login_required
def reservations_list(request):
    """ This is where we render the list of all active reservations """


    template_name = "reservations/list_reservations.html"

    reservations = Reservations.objects.filter(customer=request.user, active = "True")
    
    context = {
        'reservations' : reservations
    }

    return render(request, template_name, context)

@login_required
def reservations_list_view(request):
    """ This is where we render the list of all active reservations """


    template_name = "reservations/all_reservation_list.html"

    reservations = Reservations.objects.filter(active="True")
    
    context = {
        'reservations' : reservations
    }

    return render(request, template_name, context)

@login_required
def delete_reservations(request, pk):
    """ This is where we render deleting a specific reservations """


    obj = Reservations.objects.get(id=pk)
    obj.delete()
    return redirect('reservations:reservations_list')

                            ###################################
                            ###   Administrator Functions   ###
                            ###################################

@administrator_required()
def create_room(request):
    """ This is where we render the forms for creating new room """

    template_name = "room/create_room.html"
    form = RoomForm(request.POST or None)

    if request.method == 'POST':
        form = RoomForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully add a new room")
            return redirect('reservations:room_list')
        else:
            messages.error(request, 'Invalid input! Please check')
            form = RoomForm(request.POST or None)
    else:
        form = RoomForm(request.POST or None)

    context = { 'form' : form }

    return render(request, template_name, context)

@login_required()
def room_list(request):
    """ This is where we render the forms for creating and listing all rooms """


    template_name = "room/room_list.html"

    room = Room.objects.all()

    form = RoomForm(request.POST or None)

    if request.method == 'POST':
        form = RoomForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added a new room")
            return redirect('reservations:room_list')
        else:
            messages.error(request, 'Invalid input! Please check')
            return redirect('reservations:room_list')
    else:
        form = RoomForm(request.POST or None)


    context = { 'room' : room, 'form' : form }

    return render(request, template_name, context)


def delete_room(request, pk):
    """ This is where we render the fucntion for deleting room """

    obj = Room.objects.get(id=pk)
    obj.delete()
    messages.info(request, 'You have successfully deleted room '+" "+f'{obj.room_no}')
    
    context = {}

    return redirect('reservations:room_list')

class RoomUpdateView(BSModalUpdateView):
    model = Room
    template_name = 'room/update_room.html'
    form_class = RoomModalForm
    success_message = 'Room updated succesfully'
    success_url = reverse_lazy('reservations:room_list')


def view_customers_reservation(request):
    template_name = 'reservations/customer_reservation_list.html'

    reservations = Reservations.objects.filter(active="True")
    
    context = {
        'reservations' : reservations
    }

    return render(request, template_name, context)


def check_in_and_out(request, pk):
    template_name = 'reservations/check_in_and_out_form.html'

    customer_reservations = Reservations.objects.get(id=pk)
    reserved = get_object_or_404(Reservations, pk=pk)
    reservations = ReservationFormField(request.POST or None, instance=reserved)
    form = CheckInAndOutForm(request.POST or None)
    check_in_date = datetime.datetime.today()
    
    if form.is_valid() and reservations.is_valid():
        check_in_or_out = form.save(commit=False)
        reserved = reservations.save(commit=False)
        reserved.active = False
        check_in_or_out.reservations = customer_reservations
        check_in_or_out.check_in_date_time = check_in_date
        reserved.save()
        check_in_or_out.save()
        messages.success(request, "Transaction successfully completed")
        return redirect('reservations:list_of_check_in_or_out')
    else:
        
        form = CheckInAndOutForm(request.POST or None)

    context = {
        'form' : form
    }

    return render(request, template_name, context)

def list_of_check_in_or_out(request):
    template_name = 'reservations/check_in_or_out_list.html'

    check_in = CheckInAndOut.objects.filter(check_in="True")
    
    context = {
        'check_in' : check_in
    }

    return render(request, template_name, context)



def delete_check_in(request, pk):
    """ This is where we render the fucntion for deleting room """

    obj = CheckInAndOut.objects.get(id=pk)
    obj.delete()
    messages.info(request, 'You have successfully deleted this data')
    
    context = {}

    return redirect('reservations:list_of_check_in_or_out')


def check_out(request, pk):

    template_name = "reservations/check_out_form.html"
    customer = get_object_or_404(CheckInAndOut, pk=pk)
    
    
    form = CheckInAndOutForm(request.POST or None, instance=customer)
    check_out_date = datetime.datetime.today()
    if form.is_valid():
        check_in_or_out = form.save(commit=False)
        
        check_in_or_out.check_in_date_time = check_out_date
        check_in_or_out.save()
        messages.success(request, "Transaction successfully completed")
        return redirect('reservations:list_of_check_out')
    else:
        form = CheckInAndOutForm(request.POST or None, instance=customer)
    
    context = { 'form' : form }
    return render(request, template_name, context)



def list_of_check_out(request):
    template_name = 'reservations/check_out_list.html'

    check_in = CheckInAndOut.objects.filter(check_in="False")
    
    context = {
        'check_in' : check_in
    }

    return render(request, template_name, context)  


@login_required
def about(request):
    template_name = "reservations/about.html"

    context = {}
    
    return render(request, template_name, context)

@login_required
def contact_us(request):
    template_name = "reservations/contact_us.html"

    context = {}
    
    return render(request, template_name, context)