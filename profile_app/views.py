from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class GetProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            profile = Profile.objects.get(user=user)
            profile = ProfileSerializer(profile)

            return Response({'profile': profile.data, 'username': str(username)})
        except:
            return Response({'error': "Something went wrong when retrieving profile"})


class UpdateProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            data = self.request.data
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            image = data['image']
            about = data['about']
            birthday = data['birthday']
            socialmedia = data['socialmedia']
            profession = data['profession']
            location = data['location']

            Profile.objects.filter(user=user).update(first_name=first_name, last_name=last_name, email=email, location=location,
                                                     image=image, about=about, birthday=birthday, socialmedia=socialmedia, profession=profession)

            profile = Profile.objects.get(user=user)
            profile = ProfileSerializer(profile)

            return Response({'profile': profile.data, 'username': str(username)})
        except:
            return Response({'error': "Something went wrong when updating profile"})
