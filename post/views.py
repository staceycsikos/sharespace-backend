from rest_framework import permissions, viewsets
from .serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post




# api view needed?


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
      print ("in the first")
      return Response(serializer.data)
    else:
      print ("in the second")
      return Response(serializer.data)
    
