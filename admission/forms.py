from django import forms
from .models import YP_General_Information, Local_Authority, Care_House_Infomation, YP_Contact_Info, YP_Health_And_Wellness, YP_Physical_Description,\
    YP_Pen_Pic,YP_Banking_Information, YP_IPA, YP_Profile_Child, YP_Relationships_Associates, Profile_Pic


class YP_General_InformationForm (forms.ModelForm):
    class Meta:
        model = YP_General_Information
        fields = ['yp_first_name', 'yp_surname', 'yp_nickname', 'yp_previous_name',
                  'yp_date_of_birth', 'yp_gender', 'yp_ethnicity', 'yp_nationality', 'yp_country_origin',
                  'yp_first_language','yp_other_spoken_languages', 'local_authority', 'yp_assigned_id', 'yp_status', 'yp_uasc']

        widgets = {
            'yp_first_name': forms.TextInput (attrs={'class': 'form-control'}),
            'yp_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_nickname': forms.TextInput (attrs={'class': 'form-control'}),
            'yp_previous_name': forms.TextInput (attrs={'class': 'form-control'}),
            'yp_date_of_birth': forms.DateInput (attrs={'class': 'form-control', 'type': 'date'}),
            'yp_gender': forms.Select (attrs={'class': 'form-control'}),
            'yp_nationality': forms.Select (attrs={'class': 'form-control'}),
            'yp_first_language': forms.Select (attrs={'class': 'form-control'}),
            'yp_ethnicity': forms.Select (attrs={'class': 'form-control'}),
            'yp_country_origin': forms.Select (attrs={'class': 'form-control'}),
            'yp_other_spoken_languages': forms.Select (attrs={'class': 'form-control'}),
            'local_authority': forms.Select (attrs={'class': 'form-control'}),
            'yp_assigned_id': forms.TextInput (attrs={'class': 'form-control'}),
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
        fields = ['authority_name', 'authority_address', 'authority_address_2', 'authority_location', 'authority_postcode',  'authority_location','authority_phone', 'authority_email', 'authority_emergency_number' ]

        widgets = {
            'authority_name': forms.TextInput(attrs={'class': 'form-control'}),
            'authority_postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'authority_address': forms.TextInput(attrs={'class': 'form-control'}),
            'authority_address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'authority_location ': forms.TextInput(attrs={'class': 'form-control'}),
            'authority_email': forms.TextInput(attrs={'class': 'form-control'}),
            'authority_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'authority_emergency_number': forms.NumberInput(attrs={'class': 'form-control'})

        }

        labels = {
            'authority_name': 'Local Authority Name',
            'authority_postcode': 'Post Code',
            'authority_address': 'Address',
            'authority_address_2': 'Address Two (Optional)',
            'authority_location': 'Town',
            'authority_email': 'Placement Contact Email Address ',
            'authority_phone': 'Placement Contact Number',
            'authority_emergency_number': 'Emergency Contact  Number (out of hours)'
        }


class Care_House_InfomationForm (forms.ModelForm):
    class Meta:
        model = Care_House_Infomation
        fields = ['house_name', 'house_address_one', 'house_address_two', 'location_id', 'postcode', 'house_number','house_email', 'house_type_of_accommodation',
                  'number_of_beds','number_of_bathrooms']

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
            'house_number': 'House Mobile',
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

# Health Information


class YP_Health_And_WellnessForm(forms.ModelForm):
    class Meta:
        model = YP_Health_And_Wellness
        fields = ['yp_ability_to_make_attachments', 'yp_food_allergies', 'yp_allergies_and_attitudes', 'yp_resilience_and_self_esteem',
                  'yp_substance_misuse_issues',
                  'yp_sexual_health', 'yp_Attitude_To_Food_And_Weight', 'yp_smoking', 'yp_personal_hygiene',
                  'yp_learning_difficulties', 'yp_physical_or_sensory_impairments_and_disabilities',
                  'yp_healthcare_professional_involvement']

        widgets = {
            'yp_ability_to_make_attachments': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_food_allergies': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_allergies_and_attitudes': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_resilience_and_self_esteem': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_substance_misuse_issues': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_sexual_health': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_Attitude_To_Food_And_Weight': forms.DateInput(attrs={'class': 'form-control'}),
            'yp_smoking': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_personal_hygiene': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_learning_difficulties': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_physical_or_sensory_impairments_and_disabilities': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_healthcare_professional_involvement': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {

            'yp_ability_to_make_attachments': 'Ability to Make Attachments',
            'yp_food_allergies': 'Food Allergies',
            'yp_allergies_and_attitudes': 'Allergies and Attitude',
            'yp_resilience_and_self_esteem': 'Resilience and Self Esteem',
            'yp_substance_misuse_issues': 'Substance Misuse Issues',
            'yp_sexual_health': 'Sexual Health',
            'yp_Attitude_To_Food_And_Weight': 'Attitude to Food and Weight',
            'yp_smoking': 'Smoking',
            'yp_personal_hygiene': 'Personal Hygiene',
            'yp_learning_difficulties': 'Learning Difficulty',
            'yp_physical_or_sensory_impairments_and_disabilities': 'Physical Or Sensory Impairment and Disabilities',
            'yp_healthcare_professional_involvement': 'Health Care Professional Involvement',

        }


# Physical Description

class YP_Physical_DescriptionForm(forms.ModelForm):
    class Meta:
        model = YP_Physical_Description
        fields = ['yp_height', 'yp_weight', 'yp_build', 'yp_complexion', 'yp_eye_colour', 'yp_hair_colour',
                  'yp_marks_scars_tattoos', 'yp_disabilities',
                  'yp_relevant_medical_information', 'yp_medications']

        widgets = {
            'yp_height': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_weight': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_build': forms.Select(attrs={'class': 'form-control'}),
            'yp_complexion': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_eye_colour': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_hair_colour': forms.DateInput(attrs={'class': 'form-control'}),
            'yp_marks_scars_tattoos': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_personal_hygiene': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_disabilities': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_relevant_medical_information': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_medications': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'yp_height': 'Height (cm)',
            'yp_weight': 'Weight (kg)',
            'yp_build': 'Built',
            'yp_complexion': 'Completion',
            'yp_eye_colour': 'Eye Color',
            'yp_hair_colour': 'Hair color',
            'yp_marks_scars_tattoos': 'Marks and Tattoos',
            'yp_disabilities': 'Disabilities',
            'yp_relevant_medical_information': 'Relevant Medical Information',
            'yp_medications': 'Medication',

        }

# Banking Information


class YP_Banking_InformationForm(forms.ModelForm):
    class Meta:
        model = YP_Banking_Information
        fields = ['yp_bank', 'yp_bank_name', 'yp_bank_sort_code', 'yp_bank_account_number']

        widgets = {
            'yp_bank': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'yp_bank_sort_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'yp_bank_account_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'yp_bank': 'Bank Branch',
            'yp_bank_name': 'Bank Name',
            'yp_bank_sort_code': 'Bank Sort Code',
            'yp_bank_account_number': 'Bank Account Number',
        }

# IPA Information


class YP_IPAForm(forms.ModelForm):
    class Meta:
        model = YP_IPA
        fields = ['yp_placement_start_date', 'yp_initial_ipa_received_date', 'yp_last_ipa_start_date', 'yp_proposed_placement_end_date', 'yp_type_placement']

        widgets = {
            'yp_placement_start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Moved Into This House', 'type': 'date'}),
            'yp_initial_ipa_received_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Moved Into This House', 'type': 'date'}),
            'yp_last_ipa_start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Placement Address', 'type': 'date'}),
            'yp_proposed_placement_end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Placement Address'}),
            'yp_type_placement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type of Placement'}),

        }

        labels = {
            'yp_placement_start_date': 'Placement Start Date',
            'yp_initial_ipa_received_date': 'Initial IPA Received Date',
            'yp_last_ipa_start_date': 'Placement Address',
            'yp_proposed_placement_end_date': 'House Mobile',
            'yp_type_placement': 'Type of Placement',

        }

# Pen Picture and Background


class YP_Pen_PicForm(forms.ModelForm):
    class Meta:
        model = YP_Pen_Pic
        fields = ['yp_pen_picture','yp_pen_picture_background']

        widgets = {
            'yp_pen_picture': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pen Picture'}),
            'yp_pen_picture_background': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Background'}),


        }

        labels = {
            'yp_pen_picture': 'Pen Picture',
            'yp_pen_picture_background': 'Pen Picture Background',
        }

# Child Profile


class YP_Profile_ChildForm(forms.ModelForm):
    class Meta:
        model = YP_Profile_Child
        fields = ['yp_streghts', 'yp_achivements', 'yp_hobbies', 'personality']

        widgets = {
            'yp_streghts': forms.Textarea(attrs={'class': 'form-control'}),
            'yp_achivements': forms.Textarea(attrs={'class': 'form-control'}),
            'yp_hobbies': forms.Textarea(attrs={'class': 'form-control'}),
            'personality': forms.Textarea(attrs={'class': 'form-control'}),


        }

        labels = {
            'yp_streghts': 'Strength',
            'yp_achivements': 'Achivements',
            'yp_voice': 'Voice',
            'yp_hobbies': 'Hobbies',
            'personality': 'Personality',
        }

# Relationships and Friends

class YP_Relationships_AssociatesForm(forms.ModelForm):
    class Meta:
        model = YP_Relationships_Associates
        fields = ['next_of_kin', 'relationship_wth_next_kin', 'next_of_kin_phone', 'close_friend_name', 'contact_phone_close_friend', 'work_school_contact_phone', 'place_worship_details',
                  'places_known_frequent']

        widgets = {
            'next_of_kin': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship_wth_next_kin': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin_phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'close_friend_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone_close_friend': forms.NumberInput(attrs={'class': 'form-control'}),
            'work_school_contact_phone': forms.TextInput (attrs={'class': 'form-control'}),
            'place_worship_details': forms.TextInput(attrs={'class': 'form-control'}),
            'places_known_frequent': forms.TextInput(attrs={'class': 'form-control'}),



        }

        labels = {
            'next_of_kin': 'Next of Kin',
            'relationship_wth_next_kin': 'Relationship To Next of Kin',
            'next_of_kin_phone': 'Next of Kin Phone',
            'close_friend_name': 'Close Friends Name',
            'contact_phone_close_friend': 'Close Friends Phone',
            'place_worship_details': 'Details on Place of Worship',
            'places_known_frequent': 'Places Frequented',
            'work_school_contact_phone ': 'Work / School Phone',

        }


class Profile_PicUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile_Pic
        fields = ['image']