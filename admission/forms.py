from django import forms
from .models import YP_General_Information, Local_Authority, Profile, Care_House_Infomation, YP_Contact_Info


class YP_General_InformationForm (forms.ModelForm):
    class Meta:
        model = YP_General_Information
        fields = ['yp_first_name', 'yp_surname', 'local_authority', 'yp_assigned_id', 'yp_nickname', 'yp_previous_name',
                  'yp_date_of_birth', 'yp_gender', 'yp_ethnicity', 'yp_nationality', 'yp_country_origin',
                  'yp_first_language',
                  'yp_other_spoken_languages', 'yp_status', 'yp_uasc']

        widgets = {
            'yp_first_name': forms.TextInput (attrs={'class': 'form-control'}),
            'yp_surname': forms.TextInput (attrs={'class': 'form-control'}),
            'local_authority': forms.Select (attrs={'class': 'form-control'}),
            'yp_assigned_id': forms.TextInput (attrs={'class': 'form-control'}),
            'yp_nickname': forms.TextInput (attrs={'class': 'form-control'}),
            'yp_previous_name': forms.TextInput (attrs={'class': 'form-control'}),
            'yp_date_of_birth': forms.DateInput (attrs={'class': 'form-control', 'type': 'date'}),
            'yp_gender': forms.Select (attrs={'class': 'form-control'}),
            'yp_nationality': forms.Select (attrs={'class': 'form-control'}),
            'yp_first_language': forms.Select (attrs={'class': 'form-control'}),
            'yp_ethnicity': forms.Select (attrs={'class': 'form-control'}),
            'yp_country_origin': forms.Select (attrs={'class': 'form-control'}),
            'yp_other_spoken_languages': forms.Select (attrs={'class': 'form-control'}),
            'yp_status': forms.Select (attrs={'class': 'form-control'}),
            'yp_uasc': forms.Select (attrs={'class': 'form-control'}),

        }

        labels = {

            'yp_first_name': 'First Name',
            'yp_surname': 'Surname',
            'local_authority': 'Placing Authority',
            'yp_assigned_id': 'ID Assigned by the Council ',
            'yp_nickname': 'Nickname',
            'yp_previous_name': 'Previous Name',
            'yp_date_of_birth': 'Date of Birth',
            'yp_gender': 'Select Gender',
            'yp_nationality': 'Nationality',
            'yp_ethnicity': 'Ethnicity',
            'yp_first_language': 'First Language',
            'yp_country_origin': 'Country Origin',
            'yp_other_spoken_languages': 'Other Spoken Languages',
            'yp_status': 'Status',
            'yp_uasc': 'UASC'

        }


class Local_AuthorityForm (forms.ModelForm):
    class Meta:
        model = Local_Authority
        fields = ['authority_name', 'postcode', 'authority_address', 'authority_location', 'authority_email',
                  'authority_phone']

        widgets = {
            'authority_name': forms.TextInput (attrs={'class': 'form-control'}),
            'postcode': forms.TextInput (attrs={'class': 'form-control'}),
            'authority_address': forms.TextInput (attrs={'class': 'form-control'}),
            'authority_email': forms.TextInput (attrs={'class': 'form-control'}),
            'authority_phone': forms.TextInput (attrs={'class': 'form-control'})

        }

        labels = {
            'authority_name': 'Local Authority Name',
            'postcode': 'Post Code',
            'authority_address': 'Address',
            'authority_email': 'Email Address ',
            'authority_phone': 'Phone'
        }


class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class Care_House_InfomationForm (forms.ModelForm):
    class Meta:
        model = Care_House_Infomation
        fields = ['house_name', 'location_id', 'house_address_one', 'house_address_two', 'house_type_of_accommodation',
                  'number_of_beds',
                  'number_of_bathrooms', 'postcode', 'house_number']

        widgets = {
            'house_name': forms.TextInput (attrs={'class': 'form-control'}),
            'location_id': forms.TextInput (attrs={'class': 'form-control'}),
            'house_address_one': forms.TextInput (attrs={'class': 'form-control'}),
            'house_address_two': forms.TextInput (attrs={'class': 'form-control', 'required': False}),
            'number_of_beds': forms.Select (attrs={'class': 'form-control'}),
            'number_of_bathrooms': forms.Select (attrs={'class': 'form-control'}),
            'house_type_of_accommodation': forms.Select (attrs={'class': 'form-control'}),
            'postcode': forms.TextInput (attrs={'class': 'form-control'}),
            'house_number': forms.NumberInput (attrs={'class': 'form-control', 'required': False}),
            'house_email': forms.EmailInput (attrs={'class': 'form-control', 'required': False, }),

        }

        labels = {
            'house_name': 'House Name',
            'house_address_one': 'Address 1',
            'house_address_two': 'Address 2 (Optional)',
            'location_id': 'Town',
            'postcode': 'Postcode',
            'house_number': 'House Contact Number',
            'house_email': 'House Email',
            'number_of_beds': 'Number of Beds',
            'number_of_bathrooms': 'Number of Bathrooms',
            'house_type_of_accommodation': 'Type of House'
        }


# Contact information

class Contact_Social_DetailsForm (forms.ModelForm):
    class Meta:
        model = YP_Contact_Info
        fields = ['mobile_number', 'email_address', 'travel_card', 'facebook', 'twitter', 'snapchat', 'instagram',
                  'other']

        widgets = {
            'mobile_number': forms.NumberInput (attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput (attrs={'class': 'form-control'}),
            'travel_card': forms.RadioSelect (attrs={'class': 'form-control'}),
            'facebook': forms.URLInput (attrs={'class': 'form-control'}),
            'twitter': forms.URLInput (attrs={'class': 'form-control'}),
            'snapchat': forms.URLInput (attrs={'class': 'form-control'}),
            'instagram': forms.URLInput (attrs={'class': 'form-control'}),
            'other': forms.URLInput (attrs={'class': 'form-control'}),

        }

        labels = {
            'mobile_number': 'Phone Number',
            'email_address': 'Email Address',
            'travel_card': 'Does He/She have a Travel Card',
            'facebook': 'Facebook',
            'twitter': 'Twitter',
            'snapchat': 'SnapChat',
            'instagram': 'Instagram',
            'other': 'Other Social Media Account',
        }
