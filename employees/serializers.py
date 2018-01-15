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
    manager_url = serializers.HyperlinkedRelatedField(
        source='manager',
        read_only=True,
        view_name='employee-detail'
    )

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
            'manager_url',
            'manager',
            'office',
            'current_week_start',
            'is_active',
            'created_date',
            'positions',
        )


class EmployeeSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = (
            'id',
            'url',
            'first_name',
            'last_name'
        )


class EmployeeReadSerializer(EmployeeSerializer):
    positions = BillRateSerializer(
        many=True,
        read_only=True
    )
    # projects = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='project-detail'
    # )
    manager = EmployeeSimpleSerializer()
    # manager = serializers.HyperlinkedRelatedField(
    #     many=False,
    #     read_only=True,
    #     view_name='employee-detail'
    # )
    # office = serializers.StringRelatedField()
    # position = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='billrate-detail'
    # )