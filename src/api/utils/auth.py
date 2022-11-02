from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import serializers
from django.db import models
import secrets


def generate_access_key():
    return secrets.token_hex(128)


class AccessKey(models.Model):
    key = models.CharField(
        primary_key=True,
        max_length=256,
        default=generate_access_key)


class AccessKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessKey
        fields = ['key']


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if auth_header is None:
            raise exceptions.AuthenticationFailed('No access key provided.')

        key = auth_header.split(' ')[1]

        try:
            AccessKey.objects.get(key=key)
        except AccessKey.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid access key.')

        return (None, None)