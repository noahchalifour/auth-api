from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pathlib import Path
import os
import json

from .models import Client
from . import serializers
from .utils import auth


BASE_DIR = Path(__file__).resolve().parent.parent


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('-date_created')
    
    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CreateClientSerializer
        return serializers.ClientSerializer


class Init(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        try:
            key = auth.AccessKey.objects.get()
        except auth.AccessKey.DoesNotExist:
            key = auth.AccessKey.objects.create()

            key_filepath = os.path.join(os.environ.get('DATA_DIR', BASE_DIR), 'access_key.json')
            with open(key_filepath, 'w') as f:
                json.dump({
                    'access_key': key.key
                }, f)

        print(f'Access key = {key.key}')
        
        serializer = auth.AccessKeySerializer(key)

        return Response(serializer.data)


class Authorize(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        serializer = serializers.AuthorizeSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                "message": "Invalid request."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = Client.objects.get(
                id=serializer.data['client_id'],
                secret=serializer.data['client_secret'])

            if serializer.data['service'] not in client.services:
                return Response({
                    "message": "Client doesn't have permission to access service."
                }, status=status.HTTP_401_UNAUTHORIZED)

            return Response({})
        except Client.DoesNotExist:
            return Response({
                "message": "Invalid client."
            }, status=status.HTTP_401_UNAUTHORIZED)

        