from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from billing import models
from billing import serializers
from common.mixins.view_mixins import MultiSerializerViewSetMixin


class BillableItemsViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = models.BillableItem.objects.all()
    serializer_class = serializers.BillableItemSerializer
    serializer_action_classes = {
        'list': serializers.BillableItemReadSerializer,
        'retrieve': serializers.BillableItemReadSerializer,
    }


class BillTypesViewSet(ModelViewSet):
    queryset = models.BillType.objects.all()
    serializer_class = serializers.BillTypeSerializer


class BillRatesViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = models.BillRate.objects.all()
    serializer_class = serializers.BillRateSerializer
    serializer_action_classes = {
        'list': serializers.BillRateReadSerializer,
        'retrieve': serializers.BillRateReadSerializer,
    }


class DepartmentViewSet(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


