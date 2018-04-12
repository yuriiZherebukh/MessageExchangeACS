"""
This module contains functionality to Register, Login and get User Login status for Users
"""

import logging

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebToken

from messageExchangeACS.logger_configurations import init
from .serializers import AccountSerializer, JWTSerializer

register_log = init("E:\\Repo\MessageExchangeACS\\messageExchangeACS\\logs\\authentication.log", logging.INFO)


class ObtainJWTView(ObtainJSONWebToken):
    """
    Generates JWT and serializes it
    """

    serializer_class = JWTSerializer


class AuthRegister(APIView):
    """
    Contains functionality to register user
    """

    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        """
        Operate POST request and register User if data passed validation, otherwise return information about error
        Required data: { "email": "",
                         "first_name": "",
                         "last_name": "",
                         "password":"",
                         "confirm_password":""
                         }

        :param request: Data, sent from User request
        :param format: Include suffixes format
        :return: Result of method execution, otherwise information about error
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            register_log.debug("User registered with data: email {}, First name: {}, Last name: [}".format(
                serializer.data.get("email"), serializer.data.get("fist_name"), serializer.data.get("last_name")))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
