from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from .serializers import PostSerializer
from .models import Post


# api view needed?


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


