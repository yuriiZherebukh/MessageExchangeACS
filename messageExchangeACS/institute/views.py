from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import InstituteSerializer
from .models import Institute


class InstituteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, institute_id):
        try:
            return Institute.objects.get(pk=institute_id)
        except ObjectDoesNotExist:
            return None

    def get(self, request, institute_id=None, format=None):
        if institute_id:
            institute = self.get_object(institute_id)
            serializer = InstituteSerializer(institute)
            return Response(serializer.data)
        institutes = Institute.objects.all()
        response = InstituteSerializer(institutes, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = InstituteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, institute_id, format=None):
        institute = self.get_object(institute_id)
        serializer = InstituteSerializer(institute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, institute_id, format=None):
        institute = self.get_object(institute_id)
        institute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
