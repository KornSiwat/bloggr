import sys


from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.utils.safestring import mark_safe


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'id': 'email-field',
                'placeholder': 'Email'
            }
        ))


sys.modules[__name__] = PasswordResetForm
