import sys

from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    username = forms.CharField(
        max_length=32,
        min_length=6,
        strip=True,

        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'id': 'username-field',
                'placeholder': 'Username'
            }
        ))

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'id': 'email-field',
                'placeholder': 'Email'
            }
        ))

    password1 = forms.CharField(
        max_length=100,
        min_length=8,

        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'id': 'password-field',
                'placeholder': 'Password'
            }
        ))

    password2 = forms.CharField(
        max_length=100,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'id': 'confirm-password-field',
                'placeholder': 'Confirm Password'
            }
        ))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


sys.modules[__name__] = RegistrationForm
