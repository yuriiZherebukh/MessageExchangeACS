from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserProfileSerializer
from .models import UserProfile
from authentication.models import UserAccount


class UserProfileView(APIView):
    def get(self, request, profile_id=None, format=None):
        if profile_id:
            profile = UserProfile.get_by_id(profile_id)
            if not profile:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serialized_data = UserProfileSerializer(profile)
            return Response(serialized_data.data)
        user = UserAccount.objects.get(email=request.user)
        profile = UserProfile.get_by_id(user.pk)
        if not profile:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile_data = UserProfileSerializer(profile)
        return Response(profile_data.data)

    def put(self, request, format=None):
        user_profile = UserProfile.get_by_id(request.user.id)
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, profile_id, format=None):
        profile = UserProfile.get_by_id(profile_id)
        if not profile:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
