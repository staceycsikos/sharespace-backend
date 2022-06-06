from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

  user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  first_name = models.CharField(max_length=255, default='', blank= "False")
  last_name = models.CharField(max_length=255, default='',  blank= "False")
  image = models.CharField(max_length=500, null=True)
  email = models.CharField(max_length=500, null=True)
  about = models.TextField(max_length=500, blank=True)
  location = models.CharField(max_length=25, default='')
  birthday = models.DateField(null=True, blank=True)
  profession = models.CharField(max_length=128, blank=True)


  def __str__(self):
      return self.user_id.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()