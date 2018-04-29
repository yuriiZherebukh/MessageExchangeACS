from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from institute.models import Institute


class Department(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    floor = models.IntegerField()

    @staticmethod
    def get_by_id(department_id):
        try:
            return Department.objects.get(id=department_id)
        except ObjectDoesNotExist:
            return None
