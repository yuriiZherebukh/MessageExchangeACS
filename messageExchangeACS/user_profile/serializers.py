from rest_framework import serializers

from .models import UserProfile
from authentication.serializers import AccountSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'avatar', 'description', 'phone_number', 'position')
