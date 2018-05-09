from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from authentication.models import UserAccount

DEFAULT_AVATAR = "/static/src/img/avatar.png"


class UserProfile(models.Model):
    POSITION = (
        ('AS', 'Assistant'),
        ('EN', 'Engineer'),
        ('DC', 'Docent'),
        ('PS', 'Professor'),
        ('LA', 'laboratorian worker'),
        ('AD', 'Administrator'),
        ('SC', 'Secretary'),
        ('AC', 'Accountant'),
        ('PR', 'Pro-rector'),
        ('DP', 'Head of Department'),
        ('RC', 'Rector'),
        ('DR', 'Director'),
        )

    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, primary_key=True)
    avatar = models.URLField(default=DEFAULT_AVATAR, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    position = models.CharField(max_length=40, choices=POSITION, null=True, blank=True)

    @staticmethod
    def get_by_id(user_id):
        """
        Get user profile with user_id
        Args:
            user_id (int): id of user.
        Returns:
            Object<Profile>: Object of Profile or None if got exception.
        """
        try:
            return UserProfile.objects.get(user=user_id)
        except ObjectDoesNotExist:
            return None
