from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
  first_name = forms.CharField(max_length=255, default='', blank= "False")
  last_name = forms.CharField(max_length=255, default='',  blank= "False")
  image = forms.CharField(max_length=500, null=True)
  email = forms.CharField(max_length=500, null=True)
  about = forms.TextField(max_length=500, blank=True)
  location = forms.CharField(max_length=25, default='')
  birthday = forms.DateField(null=True, blank=True)
  profession = forms.CharField(max_length=128, blank=True)
  socialmedia = forms.URLField(max_length=500, blank=True, unique=True )  

  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'image', 'email', 'about', 'location', 'birthday', 'profession', 'socialmedia']