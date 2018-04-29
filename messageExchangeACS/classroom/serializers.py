from rest_framework import serializers

from .models import Classroom, WorkerPlace

from authentication.models import UserAccount


class ClassroomSerializer(serializers.ModelSerializer):
    workers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserAccount.objects.all()
    )

    class Meta:
        model = Classroom
        fields = ('id', 'workers', 'number', 'size')

    def create(self, validated_data):
        classroom_data = validated_data.pop("workers")
        classroom = Classroom.objects.create(**validated_data)
        for user in classroom_data:
            WorkerPlace.objects.create(worker_id=user, classroom_id=classroom)
        return classroom
