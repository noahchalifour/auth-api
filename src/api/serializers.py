from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'description', 'services', 'date_created']
        read_only_fields = ['id', 'date_created']


class CreateClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'secret', 'name', 'description', 'services']
        read_only_fields = ['id', 'secret', 'services']

    name = serializers.CharField(write_only=True)
    description = serializers.CharField(write_only=True, required=False)


class AuthorizeSerializer(serializers.Serializer):
    client_id = serializers.UUIDField()
    client_secret = serializers.CharField(max_length=128)
    service = serializers.CharField(max_length=64)