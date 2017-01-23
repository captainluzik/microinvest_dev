from django.db import models
from django.contrib import admindocs
from django.contrib.auth.models import User
#

class PhoneNumber(models.Model):
    phone_number = models.IntegerField(verbose_name='Телефон')


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', verbose_name=('User'), primary_key=True)
    phone_number = models.ForeignKey(PhoneNumber, verbose_name='Телефон')
#
