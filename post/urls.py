from django.urls import URLPattern, path
from .views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
  path('post', PostViewSet.as_view()),
 
]

urlpatterns += router.urls
