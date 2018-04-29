from rest_framework import serializers

from .models import Message, ToUser

from authentication.models import UserAccount


class MessageSerializer(serializers.ModelSerializer):
    to_users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserAccount.objects.all()
    )

    class Meta:
        model = Message
        fields = ('id', 'user', 'header', 'body', 'to_users', 'created_at')

    def create(self, validated_data):
        message_data = validated_data.pop("to_users")
        message = Message.objects.create(**validated_data)
        for user in message_data:
            ToUser.objects.create(to_user_id=user, message_id=message)
        return message

