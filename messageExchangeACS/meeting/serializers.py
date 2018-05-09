from rest_framework import serializers

from .models import Meeting
from classroom.serializers import ClassroomSerializer

from authentication.serializers import AccountSerializer


class MeetingSerializer(serializers.ModelSerializer):
    owner_user = AccountSerializer(read_only=True)
    classroom = ClassroomSerializer(read_only=True)

    class Meta:
        model = Meeting
        fields = ('id', 'owner_user', 'classroom', 'name', 'description', 'date_of_action', 'starts_at', 'finishes_at')
