from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Client
from . import serializers
from .utils import auth


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
            auth.AccessKey.objects.get()

            return Response({
                "message": "Application already initialized."
            }, status=status.HTTP_400_BAD_REQUEST)
        except auth.AccessKey.DoesNotExist:
            pass

        key = auth.AccessKey.objects.create()
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

        