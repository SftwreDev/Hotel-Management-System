from django import forms

from .models import Reservations, Room, CheckInAndOut
from bootstrap_modal_forms.forms import BSModalModelForm
import datetime
from django.utils import timezone
import pytz

utc=pytz.UTC
now = timezone.now()

class DateInput(forms.DateInput):
    input_type = 'datetime'

class TimeInput(forms.DateInput):
    input_type = 'datetime-local'

class ReservationForm(forms.ModelForm):
    room = forms.ModelChoiceField(Room.objects.filter(available = "True")) 
    class Meta :
        model = Reservations
        fields = ['check_in_datetime', 'check_out_datetime', 'hrs_to_stay', 'room']
        widgets = {
            'check_in_datetime' : TimeInput(),
            'check_out_datetime' : TimeInput(),

        }

    def clean(self):
        cleaned_data = super().clean()
        check_in_datetime = cleaned_data.get("check_in_datetime")
        check_out_datetime = cleaned_data.get("check_out_datetime")
        today = datetime.datetime.today()

        if check_in_datetime.replace(tzinfo=None) < today or check_in_datetime.replace(tzinfo=None) < today :
            raise forms.ValidationError('You cannot make a reservations on previous dates')


class ReservationFormField(forms.ModelForm):
   
    class Meta :
        model = Reservations
        fields = ['active']
      


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'



class RoomModalForm(BSModalModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class CheckInAndOutForm(forms.ModelForm):
    class Meta:
        model = CheckInAndOut
        fields = ['check_in']