from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from employees import models
from employees import serializers
from common.mixins.view_mixins import MultiSerializerViewSetMixin


class OfficesViewSet(ModelViewSet):
    queryset = models.Office.objects.all()
    serializer_class = serializers.OfficeSerializer


class EmployeesViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    serializer_action_classes = {
        'list': serializers.EmployeeReadSerializer,
        'retrieve': serializers.EmployeeReadSerializer,
    }
