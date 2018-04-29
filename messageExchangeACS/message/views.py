from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MessageSerializer
from .models import Message, ToUser


class MessageView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, message_id=None, format=None):
        if message_id:
            message = Message.get_by_id(message_id)
            if not message:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        messages = Message.objects.all()
        response = MessageSerializer(messages, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, message_id, format=None):
        message = Message.get_by_id(message_id)
        if not message:
            return Response(status=status.HTTP_404_NOT_FOUND)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
