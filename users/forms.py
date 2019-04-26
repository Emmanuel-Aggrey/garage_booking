from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mysite.models import Servicings


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class CreateBookingForm():
    service_type = forms.CharField()
    service_description = forms.TextInput()
    service_location = forms.CharField()

    class Meta:
        model = Servicings
        fields = ['service_type', 'service_description', 'service_location']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']