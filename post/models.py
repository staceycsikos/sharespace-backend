from django.db import models
from profile_app.models import Profile
from django.utils import timezone

class Post(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_profile')
  post = models.TextField(max_length=500, blank=False)
  publish_date = models.DateTimeField(default=timezone.now, blank=True)

  def __str__(self):
    return self.profile.user_id.username

