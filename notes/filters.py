import django_filters
from django import forms
from .models import Notes, YP_General_Information


class YP_Notes_Month_Filter (django_filters.FilterSet):
    yp = django_filters.ModelChoiceFilter(label='Young Adult Name',queryset=YP_General_Information.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Young Adult'}),)
    min_date = django_filters.DateTimeFilter(label='Start Date', field_name='date_notes', lookup_expr='gte',
                                             widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Maximum Date', 'type': 'date'}), )
    max_date = django_filters.DateTimeFilter(label='End Date', field_name='date_notes', lookup_expr='lte',
                                             widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Minimum Date', 'type': 'date'}), )

    class Meta:
        model = Notes
        fields = ['yp', 'min_date', 'max_date']


class Child_Notes_Month_Filter (django_filters.FilterSet):
    min_date = django_filters.DateTimeFilter(label='Start Date', field_name='date_notes', lookup_expr='gte',
                                             widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Maximum Date', 'type': 'date'}), )
    max_date = django_filters.DateTimeFilter(label='End Date', field_name='date_notes', lookup_expr='lte',
                                             widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Minimum Date', 'type': 'date'}), )

    class Meta:
        model = Notes
        fields = ['min_date', 'max_date']
