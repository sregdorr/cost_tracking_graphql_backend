from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from clients.models import Client, Contact
from clients import serializers
from common.mixins.view_mixins import MultiSerializerViewSetMixin


class ContactsViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class ClientsViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    serializer_action_classes = {
        'list': serializers.ClientReadSerializer,
        'retrieve': serializers.ClientReadSerializer
    }
