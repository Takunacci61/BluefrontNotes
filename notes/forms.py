from django import forms
from .models import Notes, Parent_Notes


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

    # Parent Forms


class Parent_NotesForm(forms.ModelForm):
    class Meta:
        model = Parent_Notes
        fields = ['date_notes', 'time_start', 'time_end', 'location_id', 'contact_type', 'question_1a', 'question_1b', 'question_1c', 'question_1d',
                  'question_1e', 'question_1f', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6', 'question_7', 'question_8',
                  'detailed_notes']

        widgets = {
            'date_notes': forms.DateInput(attrs={'class': 'form-control input-sm', 'type': 'date'}),
            'time_start': forms.TimeInput(attrs={'class': 'form-group input-sm', 'type': 'time'}),
            'time_end': forms.TimeInput(attrs={'class': 'form-group input-sm', 'type': 'time'}),
            'location_id': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'contact_type': forms.Select(attrs={'class': 'form-control input-sm'}),
            'question_1a': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_1b': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_1c': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_1d': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_1e': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_1f': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_2': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_3': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_4': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_5': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_6': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_7': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'question_8': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            'detailed_notes': forms.Textarea(attrs={'class': 'form-control input-sm'}),
        }

        labels = {
            'date_notes': 'Contact Date',
            'time_start': 'Contact Start Time',
            'time_end': 'Contact End Time',
            'location_id': 'Contact Location',
            'contact_type': 'Contact Type',
            'question_1a': 'Contact Type',
            'question_1b': 'Contact Type',
            'question_1c': 'Contact Type',
            'question_1d': 'Contact Type',
            'question_1e': 'Contact Type',
            'question_2': 'Contact Type',
            'question_3': 'Contact Type',
            'question_4': 'Contact Type',
            'question_5': 'Contact Type',
            'question_6': 'Contact Type',
            'question_7': 'Contact Type',
            'question_8': 'Contact Type',
            'detailed_notes': 'Detailed Notes',
        }