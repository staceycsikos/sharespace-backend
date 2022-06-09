from rest_framework import permissions, viewsets
from .serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post


class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  @action(detail=True, methods=['post'])
  def create(self, request, pk=None):
    print (request.data)
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response("error possibly this guy right?")
    
