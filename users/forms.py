from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm


class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm (forms.ModelForm):
    email = forms.EmailField ()

    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {

            'username': forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput (attrs={'class': 'form-control'}),
        }

        labels = {

            'username': 'Username',
            'email': 'Email',

        }


class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


# Login Class


class UserLoginForm (AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), label='')


class UserPasswordResetForm (PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label='')
