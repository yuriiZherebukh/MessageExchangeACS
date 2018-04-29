from rest_framework import serializers

from .models import Institute


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ('id', 'header', 'boxy', 'created_at')
