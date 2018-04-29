from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from institute.models import Institute
from department.models import Department


class Group(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)

    @staticmethod
    def get_by_id(group_id):
        try:
            return Group.objects.get(id=group_id)
        except ObjectDoesNotExist:
            return None
