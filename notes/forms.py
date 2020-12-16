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
            'question_1a': 'Breakfast',
            'question_1b': 'Morning Snack',
            'question_1c': 'Lunch',
            'question_1d': 'Mid Afternoon snack',
            'question_1e': 'Supper',
            'question_1f': 'Bedtime',
            'question_2': 'What times was baby’s nappy changed and by who ?',
            'question_3': 'Has baby had a bath during the shift ?',
            'question_4': 'Please provide full documentation of conversations with the parent ',
            'question_5': 'Any safeguarding concerns please specify and report immediately to as per protocol ',
            'question_6': 'What times did baby sleep and how long for ?',
            'question_7': 'What time did Parent and baby leave and return from placement',
            'question_8': 'Has baby been appropriately stimulated by the parent ?',
            'detailed_notes': 'Detailed Notes',
        }