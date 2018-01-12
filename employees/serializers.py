from rest_framework import serializers

from employees import models
from billing.serializers import BillRateSerializer


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Office
        fields = (
            'id',
            'url',
            'description',
            'address',
            'city',
            'state',
            'zip_code',
            'phone',
            'is_active',
            'created_date',
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = (
            'id',
            'url',
            'first_name',
            'last_name',
            'middle_initial',
            'email',
            'cell_phone',
            'office_phone',
            'office_ext',
            'manager',
            'office',
            'current_week_start',
            'is_active',
            'created_date',
            'position',
            'projects',
        )


class EmployeeReadSerializer(EmployeeSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='project-detail'
    )
    manager = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='employee-detail'
    )
    office = serializers.StringRelatedField()
    position = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='billrate-detail'
    )