from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GroupSerializer
from .models import Group
from institute.models import Institute
from department.models import Department


class GroupView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request,  institute_id=None, department_id=None, group_id=None, format=None):
        if group_id:
            group = Group.get_by_id(group_id)
            if not group:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serialized_data = GroupSerializer(group)
            return Response(serialized_data.data)
        institute = Institute.get_by_id(institute_id)
        department = Department.get_by_id(department_id)
        groups = Group.objects.filter(institute=institute, department=department)
        return Response(groups.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, group_id, format=None):
        group = Group.get_by_id(group_id=group_id)
        if not group:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, group_id, format=None):
        group = Group.get_by_id(group_id)
        if not group:
            return Response(status=status.HTTP_404_NOT_FOUND)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
