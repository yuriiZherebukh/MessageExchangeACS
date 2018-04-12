from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Institute(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house_number = models.IntegerField()

    @staticmethod
    def get_by_id(institute_id):
        try:
            return Institute.objects.get(id=institute_id)
        except ObjectDoesNotExist:
            return None
