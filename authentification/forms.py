from django import forms
from authentification.models import FineUser  # Import your custom user model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = FineUser  # Use your custom user model here
        fields = ['email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
