from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from common.mixins.view_mixins import MultiSerializerViewSetMixin
from invoicing.models import InvoiceStatus, Invoice
from invoicing import serializers


class InvoiceStatusesViewSet(ModelViewSet):
    queryset = InvoiceStatus.objects.all()
    serializer_class = serializers.InvoiceStatusSerializer


class InvoicesViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    serializer_action_classes = {
        'list': serializers.InvoiceReadSerializer,
        'retrieve': serializers.InvoiceReadSerializer,
    }
