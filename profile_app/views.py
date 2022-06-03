from django.shortcuts import render
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer


## similar to line 19 seems like we need a specific user 
class GetProfileView(APIView):
    def get(self, request, format=None):
      try:
        user = self.request.user

        username = user.username

        current_user = User.objects.get(id= user.id)
        profileval_app = Profile.objects.get(user_id = user)

        # profile = Profile.objects.get(user=user)
        # profile = ProfileSerializer(profile)

        profile_app = ProfileSerializer(profileval_app)

        return Response({'profile': profile_app.data, 'username': str(username)})
      except:
        return Response({'error': "Something went wrong when retrieving profile"})

# similar to line 35
class UpdateProfileView(APIView):
  def put(self, request, format=None):
    try:
        user = self.request.user
        username = user.username

        data = self.request.data
            # first_name = data['first_name']
            # last_name = data['last_name']
            # email = data['email']
            # image = data['image']
            # about = data['about']
            # birthday = data['birthday']
            # socialmedia = data['socialmedia']
            # profession = data['profession']
            # location = data['location']

        current_user = User.objects.get( id = user.id)
        # print(current_user)

        
        # updatedProfile = 
        Profile.objects.filter(user_id = current_user).update(first_name=data['first_name'],last_name=data['last_name'], email=data['email'], location=data['location'], image=data['image'], about=data['about'], birthday=data['birthday'], socialmedia=data['socialmedia'], profession=data['profession'])
        profileval_app = Profile.objects.get(user_id = user)
        profile_app = ProfileSerializer(profileval_app)
        return Response({'profile': profile_app.data, 'username': str(username)})
    except:
        return Response({'error': "Something went wrong when updating profile"})

#similar to line 56, seems like to get all profiles
class GetProfilesView(APIView):
  permission_classes = (permissions.AllowAny,)

  def get(self, request, format=None):
      profiles = Profile.objects.all()

      profiles = ProfileSerializer(profiles, many=True)
      return Response(profiles.data)


            # Profile.objects.filter(user = current_user).update(first_name=data['first_name']).save()
            # last_name=data['last_name'], email=data['email'], location=data['location'],
            #                                         image=data['image'], about=data['about'], birthday=data['birthday'], socialmedia=data['socialmedia'], profession=data['profession'])
             
            # print (current_user)
            # Profile.objects.filter(user=user).update(first_name=first_name, last_name=last_name, email=email, location=location,
            #                                          image=image, about=about, birthday=birthday, socialmedia=socialmedia, profession=profession)

        #     profileval = Profile.objects.get(user=user)
        #     profile = ProfileSerializer(profileval)

        #     print(profileval)

        #     return Response({'profile': profile.data, 'username': str(username)})
        # except:
        #     return Response({'error': "Something went wrong when updating profile"})



# WE DO NOT HAVE THESE LINKEDFIN DOES

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = User_profile.objects.all()
#     serializer_class = ProfileSerializer
