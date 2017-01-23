from registration.signals import user_registered, user_activated
from .models import Profile, PhoneNumber
from .forms import RegistrationFormProfile
from django.contrib import auth



def user_created(sender, user, request, **kwargs):
    form = RegistrationFormProfile(request.POST)
    profile = Profile(user=user, phone_number_id=int(form.data['phone_number']))
    profile.save()


def login_on_activation(sender, user, request, **kwargs):
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)


user_activated.connect(login_on_activation)
user_registered.connect(user_created)
