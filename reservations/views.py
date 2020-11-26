from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import customer_required, personnel_required, administrator_required
from .forms import ReservationForm, RoomForm
from .models import Reservations, Room

def homepage(request):
    """ This is where we render the homepage og this system """


    template_name = "reservations/home.html"

    context = {}

    return render(request, template_name, context)


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


def reservations_list(request):
    """ This is where we render the list of all active reservations """


    template_name = "reservations/list_reservations.html"

    reservations = Reservations.objects.filter(customer=request.user)
    
    context = {
        'reservations' : reservations
    }

    return render(request, template_name, context)


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
    messages.info(request, 'You have successfully delete a room')
    
    context = {}

    return redirect('reservations:room_list')