
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from post.views import PostViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list','post': 'create'})),
    path('admin/', admin.site.urls),
    path('profile/', include('profile_app.urls')),
    path('', include('api_app.urls')),
    path('api_auth/', include('rest_framework.urls')),
]

# Add regular expression for catch-all

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]