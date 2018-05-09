from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MeetingSerializer
from .models import Meeting, ParticipatedUser

from authentication.models import UserAccount
from classroom.models import Classroom


class MeetingView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, meeting_id=None, owner=False, format=None):
        if meeting_id:
            meeting = Meeting.get_by_id(meeting_id)
            if not meeting:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MeetingSerializer(meeting)
            return Response(serializer.data)
        if owner:
            meetings = Meeting.objects.filter(owner_user=request.user)
            response = MeetingSerializer(meetings, many=True)
            return Response(response.data)
        meetings = Meeting.objects.filter(participateduser__participated_user=request.user)
        response = MeetingSerializer(meetings, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        data_request = request.data
        participated_users_list = data_request.pop("participated_user")
        classroom = Classroom.get_by_id(data_request.pop("classroom"))
        serializer = MeetingSerializer(data=data_request)
        if serializer.is_valid():
            serializer.save(owner_user=request.user, classroom=classroom)
            for participated_user in participated_users_list:
                user_instance = UserAccount.objects.get(pk=participated_user)
                meeting_instance = Meeting.get_by_id(serializer.data.get("id"))
                participated_user_instance = ParticipatedUser.objects.create(participated_user=user_instance,
                                                                             meeting=meeting_instance)
                participated_user_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, meeting_id=None):
        if meeting_id:
            meeting = Meeting.get_by_id(meeting_id)
            if not meeting:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MeetingSerializer(meeting)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, meeting_id, format=None):
        meeting = Meeting.get_by_id(meeting_id)
        if not meeting:
            return Response(status=status.HTTP_404_NOT_FOUND)
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
