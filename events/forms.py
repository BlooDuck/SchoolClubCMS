from django import forms
from django.forms import ModelForm
from .models import Event


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateForm(ModelForm):

    class Meta:
        model = Event
        fields = ['user', 'event_name', 'location', 'date', 'start_time', 'end_time', 'club' , 'description' ]
        widgets = {
            'date': DateInput(),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'})
        }
