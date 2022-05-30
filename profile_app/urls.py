from django.urls import path
from .views import GetProfileView, UpdateProfileView, GetProfilesView


urlpatterns = [
    path('user', GetProfileView.as_view()),
    path('update', UpdateProfileView.as_view()),
    path('all', GetProfilesView.as_view())
]