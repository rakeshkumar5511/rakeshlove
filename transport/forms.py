from django import forms
from .models import BusLocation, PassengerCount


class BusLocationForm(forms.ModelForm):
    class Meta:
        model = BusLocation
        fields = ['bus', 'latitude', 'longitude', 'speed']
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': 'any', 'readonly': 'readonly'}),
            'longitude': forms.NumberInput(attrs={'step': 'any', 'readonly': 'readonly'}),
            'speed': forms.NumberInput(attrs={'step': 'any'}),
        }


class PassengerCountForm(forms.ModelForm):
    class Meta:
        model = PassengerCount
        fields = ['bus', 'current_count', 'in_count', 'out_count']