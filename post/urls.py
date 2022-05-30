from django.urls import URLPattern, path
from .views import PostViewSet
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'post', PostViewSet)

router = routers.DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
# urlpatterns = router.urls

# urlpatterns = [
#   path('post', PostViewSet.as_view({'get': 'list'})),
 
# ]

# urlpatterns += router.urls
