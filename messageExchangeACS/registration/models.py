"""
Contains Models for User and Registration
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=254, blank=True, null=True)
    last_name = models.CharField(max_length=254, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=254, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    USERNAME_FIELD = 'email'  # This constant defines username field to be returned after calling User object
    objects = BaseUserManager()

    @staticmethod
    def create(email, password, first_name=None, last_name=None):
        custom_user = CustomUser()
        custom_user.email = email
        custom_user.set_password(password)
        custom_user.first_name = first_name
        custom_user.last_name = last_name
        custom_user.save()
        return custom_user

    def change_password(self, password):
        self.set_password(password)
        self.save()

    @staticmethod
    def get_by_id(user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            return user
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def get_by_email(email):
        try:
            user = CustomUser.objects.get(email=email)
            return user
        except CustomUser.DoesNotExist:
            return None

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        if self.last_name:
            return self.last_name
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            full_name = '{} {}'.format(self.first_name, self.last_name)
            return full_name

    def update(self, first_name=None, last_name=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        self.save()

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'create_at': self.create_at,
            'update_at': self.update_at
        }

    @staticmethod
    def email_validation(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False