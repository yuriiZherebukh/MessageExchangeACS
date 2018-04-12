from rest_framework import serializers

from .models import Institute


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ('id', 'name', 'city', 'street', 'house_number')
