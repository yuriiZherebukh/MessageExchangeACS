from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import UserAccount


class Message(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='sender_user')
    header = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_by_id(message_id):
        try:
            return Message.objects.get(id=message_id)
        except ObjectDoesNotExist:
            return None


class ToUser(models.Model):
    to_user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    message = models.ForeignKey(Message)
