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
    
    class Meta :
        model = Reservations
        fields = ['name','address','email_address','contact','type_of_id','id_no','no_of_days','check_in_datetime', 'check_out_datetime', 'room']
        widgets = {
            'check_in_datetime' : TimeInput(),
            'check_out_datetime' : TimeInput(),

        }

    def clean(self):
        cleaned_data = super().clean()
        check_in_datetime = cleaned_data.get("check_in_datetime")
        check_out_datetime = cleaned_data.get("check_out_datetime")
        today = datetime.datetime.today()

        if check_in_datetime.replace(tzinfo=None) < today or check_out_datetime.replace(tzinfo=None) < today:
            raise forms.ValidationError('You cannot make a reservations on previous dates')
        elif  check_out_datetime < check_in_datetime :
            raise forms.ValidationError('Invalid input on check out date')

         # if check_in_date < today or check_out_date < today:
        #     raise forms.ValidationError('You cannot make a reservations on previous dates')
        # if  check_out_date < check_in_date :
        #     raise forms.ValidationError('Invalid input on check out date')

        # if check_in_time < time or check_out_time < time:
        #     raise forms.ValidationError('You cannot make a reservations on previous time')
        # if  check_out_time < check_in_time :
        #     raise forms.ValidationError('Invalid input on check out time')

class ReservationFormField(forms.ModelForm):
   
    class Meta :
        model = Reservations
        fields = ['active']
      

class SelectRoomForm(forms.ModelForm):
    room = forms.ModelChoiceField(Room.objects.filter(available = "True")) 
    class Meta:
        model = Reservations
        fields = ['room']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class RoomFormField(forms.ModelForm):
    
    class Meta:
        model = Room
        fields = ['available']

class RoomModalForm(BSModalModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class CheckInAndOutForm(forms.ModelForm):
    class Meta:
        model = CheckInAndOut
        fields = ['check_in']