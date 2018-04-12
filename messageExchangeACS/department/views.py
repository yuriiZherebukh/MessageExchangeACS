from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DepartmentSerializer
from .models import Department
from institute.models import Institute


class InstituteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, department_id):
        try:
            return Department.objects.get(pk=department_id)
        except ObjectDoesNotExist:
            return None

    def get(self, request, department_id, format=None):
        department = self.get_object(department_id)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def post(self, request, institute_id=None, format=None):
        # institute = Institute.get_by_id(institute_id)
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, department_id, format=None):
        department = self.get_object(department_id)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, department_id, format=None):
        department = self.get_object(department_id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
