"""
This module contains classes to serialize Authentication app models
"""

from django.contrib.auth import authenticate, user_logged_in
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler

from .models import UserAccount


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializes User account model
    """
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        """
        Contains meta data of User Account serializer
        """
        model = UserAccount
        fields = (
            'id', 'email', 'date_created', 'date_modified',
            'first_name', 'last_name', 'password', 'confirm_password')
        read_only_fields = ('date_created', 'date_modified')

    def create(self, validated_data: dict):
        """
        Call User account create method

        :param validated_data: User Account data
        :return: Result of method execution
        """
        return UserAccount.objects.create_user(**validated_data)

    def update(self, instance: UserAccount, validated_data: dict):
        """
        Update User Account instance data

        :param instance: User account data
        :param validated_data: User Account data to update
        :return: User account object
        """
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and password == confirm_password:
            instance.set_password(password)

        instance.save()
        return instance

    def validate(self, data: dict):
        """
        Check if User Account password is equal as password confirm

        :param data:
        :return: User Account data, otherwise False
        """
        if data['password']:

            if data['password'] != data['confirm_password']:
                return False
        return data

    def get_by_id(self, user_id):
        try:
            return UserAccount.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None


class JWTSerializer(JSONWebTokenSerializer):
    """
    Serializes JWT data
    """
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(request=self.context['request'], **credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)
                user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)
