from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import UserAccount
from classroom.models import Classroom


class Meeting(models.Model):
    owner_user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='created_user')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date_of_action = models.DateField(editable=True, null=True, blank=True)
    starts_at = models.TimeField(editable=True, null=True, blank=True)
    finishes_at = models.TimeField(editable=True, null=True, blank=True)

    @staticmethod
    def get_by_id(meeting_id):
        try:
            return Meeting.objects.get(id=meeting_id)
        except ObjectDoesNotExist:
            return None


class ParticipatedUser(models.Model):
    participated_user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
