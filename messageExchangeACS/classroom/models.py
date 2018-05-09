from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import UserAccount


class Classroom(models.Model):
    number = models.IntegerField()
    size = models.IntegerField()

    @staticmethod
    def get_by_id(classroom_id):
        try:
            return Classroom.objects.get(id=classroom_id)
        except ObjectDoesNotExist:
            return None
