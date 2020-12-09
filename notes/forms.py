from django import forms
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['date_notes', 'time_start', 'time_end', 'location_id', 'contact_type', 'detailed_notes']

        widgets = {
            'date_notes': forms.DateInput(attrs={'class': 'form-control input-sm', 'type': 'date'}),
            'time_start': forms.TimeInput(attrs={'class': 'form-group input-sm', 'type': 'time'}),
            'time_end': forms.TimeInput(attrs={'class': 'form-group input-sm', 'type': 'time'}),
            'location_id': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'contact_type': forms.Select(attrs={'class': 'form-control input-sm'}),
            'detailed_notes': forms.Textarea(attrs={'class': 'form-control input-sm'}),
        }

        labels = {
            'date_notes': 'Contact Date',
            'time_start': 'Contact Start Time',
            'time_end': 'Contact End Time',
            'location_id': 'Contact Location',
            'contact_type': 'Contact Type',
            'detailed_notes': 'Detailed Notes',
        }


class Notes_Month_FilterForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['yp', 'date_notes']

        widgets = {
            'yp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Young Person'}),
            'date_notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date Range', 'id': 'finish'}),

        }

        labels = {
            'yp': 'Please Select The Young Person',
            'date_notes': 'Date Range',
        }