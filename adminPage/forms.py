from django import forms
from django.forms import DateInput
from django.forms import FileInput
from Bus.models import Bus, Seat

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'
        widgets = {
            'travel_dates': DateInput(attrs={'type': 'date'}),
            'image': FileInput(attrs={'type': 'file'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get('source')
        destination = cleaned_data.get('destination')

        if source and destination and source == destination:
            raise forms.ValidationError("Source and destination cannot be the same.")

        return cleaned_data


class SeatForm(forms.Form):
    selected_seats = forms.CharField(widget=forms.HiddenInput())
