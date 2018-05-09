from rest_framework import serializers

from authentication.serializers import AccountSerializer

from .models import Message


class MessageSerializer(serializers.ModelSerializer):

    user = AccountSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'user', 'header', 'body', 'created_at')

