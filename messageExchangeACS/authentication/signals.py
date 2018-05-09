import logging

from django.contrib.auth import user_logged_in, user_login_failed
from django.dispatch import receiver

from .models import UserLoginActivity
from .utils import get_client_ip

error_log = logging.getLogger()


@receiver(user_logged_in)
def log_user_logged_in_success(sender, user, request, **kwargs):
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log = UserLoginActivity(login_IP=get_client_ip(request),
                                                    login_username=user.email,
                                                    user_agent_info=user_agent_info,
                                                    status=UserLoginActivity.SUCCESS)
        user_login_activity_log.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in_success request: %s, error: %s" % (request, e))


@receiver(user_login_failed)
def log_user_logged_in_failed(sender, credentials, request, **kwargs):
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log = UserLoginActivity(login_IP=get_client_ip(request),
                                                    login_username=credentials['username'],
                                                    user_agent_info=user_agent_info,
                                                    status=UserLoginActivity.FAILED)
        user_login_activity_log.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in_failed request: %s, error: %s" % (request, e))
