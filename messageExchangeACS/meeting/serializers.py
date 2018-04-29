from rest_framework import serializers

from .models import Meeting, ParticipatedUser

from authentication.models import UserAccount


class MeetingSerializer(serializers.ModelSerializer):
    participated_user = serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserAccount.objects.all()
    )

    class Meta:
        model = Meeting
        fields = ('id', 'owner_user', 'classroom', 'participated_user', 'date_of_action', 'starts_at', 'finishes_at')

    def create(self, validated_data):
        meeting_data = validated_data.pop("participated_user")
        meeting = Meeting.objects.create(**validated_data)
        for participated_user in meeting_data:
            ParticipatedUser.objects.create(participated_user_id=participated_user, meeting_id=meeting_data)
        return meeting
