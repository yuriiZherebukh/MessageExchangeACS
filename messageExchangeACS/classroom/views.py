from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ClassroomSerializer
from .models import Classroom


class ClassroomView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, classroom_id=None, format=None):
        if classroom_id:
            classroom = Classroom.get_by_id(classroom_id)
            if not classroom:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClassroomSerializer(classroom)
            return Response(serializer.data)
        classrooms = Classroom.objects.all()
        response = ClassroomSerializer(classrooms, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, classroom_id=None):
        if classroom_id:
            classroom = Classroom.get_by_id(classroom_id)
            if not classroom:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClassroomSerializer(classroom)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, classroom_id, format=None):
        classroom = Classroom.get_by_id(classroom_id)
        if not classroom:
            return Response(status=status.HTTP_404_NOT_FOUND)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
