"""
Contains models to operate with User account and User login activity
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    """
    Contains functionality to operate with User registration
    """

    def create_user(self, email: str, password: str = None, **kwargs):
        """
        Create User model

        :param email: User's email
        :param password: User's password
        :param kwargs: Kwargs, sent from views
        :return: User object
        """
        account = self.model(
            email=self.normalize_email(email),
            first_name=kwargs.get('first_name', None),
            last_name=kwargs.get('last_name', None), )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password=None, **kwargs):
        """
        Create user with administrators rights

        :param email: User's email
        :param password: User's password
        :param kwargs: Kwargs, sent from views
        :return: Administrator object
        """

        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class UserAccount(AbstractBaseUser):
    """
    Class model with User account
    """
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class UserLoginActivity(models.Model):
    """
    Contains models for User login activity
    """
    SUCCESS = 'S'
    FAILED = 'F'

    LOGIN_STATUS = ((SUCCESS, 'Success'),
                    (FAILED, 'Failed'))

    login_IP = models.GenericIPAddressField(null=True, blank=True)
    login_datetime = models.DateTimeField(auto_now=True)
    login_username = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=1, default=SUCCESS, choices=LOGIN_STATUS, null=True, blank=True)
    user_agent_info = models.CharField(max_length=255)

    class Meta:
        """
        Contains meta data of User login activity model
        """
        verbose_name = 'user_login_activity'
        verbose_name_plural = 'user_login_activities'
