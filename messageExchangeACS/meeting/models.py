from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import UserAccount
from classroom.models import Classroom


class Meeting(models.Model):
    owner_user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='created_user')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    participated_user = models.ManyToManyField(UserAccount, through='ParticipatedUser')
    created_at = models.DateTimeField(auto_now_add=True)
    date_of_action = models.DateTimeField(editable=True, null=True, blank=True)
    starts_at = models.DateTimeField(editable=True, null=True, blank=True)
    finishes_at = models.DateTimeField(editable=True, null=True, blank=True)

    @staticmethod
    def get_by_id(meeting_id):
        try:
            return Meeting.objects.get(id=meeting_id)
        except ObjectDoesNotExist:
            return None


class ParticipatedUser(models.Model):
    participated_user_id = models.ForeignKey(UserAccount)
    meeting_id = models.ForeignKey(Meeting)
