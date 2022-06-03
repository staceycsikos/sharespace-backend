from django.db import models
from profile_app.models import Profile
# Create your models here.
class Auth(models.Model):
  profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user')