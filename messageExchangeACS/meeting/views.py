from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MeetingSerializer
from .models import Meeting


class MeetingView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, meeting_id=None, format=None):
        if meeting_id:
            meeting = Meeting.get_by_id(meeting_id)
            if not meeting:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MeetingSerializer(meeting)
            return Response(serializer.data)
        meetings = Meeting.objects.all()
        response = MeetingSerializer(meetings, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
