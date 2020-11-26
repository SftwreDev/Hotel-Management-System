from django import forms

from .models import Reservations, Room

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'

class ReservationForm(forms.ModelForm):
    class Meta :
        model = Reservations
        fields = ('check_in', 'check_out', 'arrival_date', 'departure_date', 'hrs_to_stay', 'room')
        widgets = {
            'arrival_date' : DateInput(),
            'departure_date' : DateInput(),
            'check_in' : TimeInput(),
            'check_out' : TimeInput(),

        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'