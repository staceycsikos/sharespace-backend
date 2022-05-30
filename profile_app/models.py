from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=255, default='', blank= "False")
  last_name = models.CharField(max_length=255, default='',  blank= "False")
  image = models.CharField(max_length=500, null=True)
  email = models.CharField(max_length=500, null=True)
  about = models.TextField(max_length=500, blank=True)
  location = models.CharField(max_length=25, default='')
  birthday = models.DateField(null=True, blank=True)
  profession = models.CharField(max_length=128, blank=True)
  socialmedia = models.URLField(max_length=500, blank=True, unique=True )  

  def __str__(self):
      return self.first_name