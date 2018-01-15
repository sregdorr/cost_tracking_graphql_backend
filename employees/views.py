from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from employees import models
from employees import serializers
from common.mixins.view_mixins import MultiSerializerViewSetMixin
from rest_framework_extensions.mixins import NestedViewSetMixin


class OfficesViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = models.Office.objects.all()
    serializer_class = serializers.OfficeSerializer


class EmployeesViewSet(NestedViewSetMixin, MultiSerializerViewSetMixin, ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    serializer_action_classes = {
        'list': serializers.EmployeeReadSerializer,
        'retrieve': serializers.EmployeeReadSerializer,
    }

    # def list(self, request, office_pk=None, *args, **kwargs):
    #     if office_pk is None:
    #         queryset = self.get_queryset()
    #     else:
    #         queryset = models.Employee.objects.filter(office=office_pk)
    #     serializer = serializers.EmployeeSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)

