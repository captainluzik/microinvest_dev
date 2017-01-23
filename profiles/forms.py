from django import forms
from registration.forms import RegistrationFormUniqueEmail
from .models import PhoneNumber

class RegistrationFormProfile(RegistrationFormUniqueEmail):
    phone = forms.IntegerField(label='Телефон')
#