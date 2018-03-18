import logging
from json import loads

from django.contrib import auth

from .constants import *
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        data = loads(request.body.decode('utf-8'))
        email = data.get("email").lower()
        password = data.get("password")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        if not email or not password:
            return response_400_required

        if not CustomUser.email_validation(email):
            return response_400_invalid_format

        if CustomUser.get_by_email(email):
            return response_400_already_registered

        user = CustomUser.create(email=email, password=password,
                                 first_name=first_name, last_name=last_name)
        if not user:
            return response_400_invalid_format

        # todo: Add email notification for user confirm

        return response_201_successfully_created


def login(request):
    if request.method == 'POST':
        logging.info(request)
        data = loads(request.body.decode('utf-8'))
        email = data.get("email").lower()
        password = data.get("password")
        user = auth.authenticate(username=email, password=password)
        if user:
            auth.login(request, user)
            response = response_200_login_successful
            response.set_cookie('user_id', user.id)
            return response
        return response_403_invalid_credentials


def logout(request):
    if request.method == 'GET':
        logging.debug(request)
        if request.user.is_authenticated():
            auth.logout(request)
            response = response_200_logout_successful
            response.delete_cookie('user_id')
            response.delete_cookie('facebook-token')
            return response
        return response_400_not_logged_in

