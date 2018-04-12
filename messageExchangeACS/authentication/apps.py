"""
This module imports signals to project, that handles User login success and failure
"""

from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Contains functionality to register signals
    """
    name = 'authentication'

    def ready(self):
        from .signals import log_user_logged_in_failed, log_user_logged_in_success
