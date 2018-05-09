from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.models import UserAccount

from .serializers import MessageSerializer
from .models import Message, ToUser


class MessageView(APIView):
    def get(self, request, message_id=None, sent=False, format=None):
        if message_id:
            message = Message.get_by_id(message_id)
            if not message:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        if sent:
            messages = Message.objects.filter(user=request.user)
            response = MessageSerializer(messages, many=True)
            return Response(response.data)
        messages = Message.objects.filter(touser__to_user=request.user)
        response = MessageSerializer(messages, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        data_request = request.data
        to_users_list = data_request.pop("to_users")
        serializer = MessageSerializer(data=data_request)
        if serializer.is_valid():
            serializer.save(user=request.user)
            for to_user in to_users_list:
                user_instance = UserAccount.objects.get(pk=to_user)
                message_instance = Message.get_by_id(serializer.data.get("id"))
                to_user_instance = ToUser.objects.create(to_user=user_instance, message=message_instance)
                to_user_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, message_id, format=None):
        message = Message.get_by_id(message_id)
        if not message:
            return Response(status=status.HTTP_404_NOT_FOUND)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
