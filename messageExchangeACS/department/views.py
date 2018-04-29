from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DepartmentSerializer
from .models import Department


class InstituteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, department_id=None, format=None):
        if department_id:
            department = Department.get_by_id(department_id)
            if not department:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        departments = Department.objects.all()
        response = DepartmentSerializer(departments, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, department_id, format=None):
        department = Department.get_by_id(department_id)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, department_id, format=None):
        department = Department.get_by_id(department_id)
        if not department:
            return Response(status=status.HTTP_404_NOT_FOUND)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
