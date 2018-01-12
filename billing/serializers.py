from rest_framework import serializers

from billing import models


class BillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BillType
        fields = (
            'id',
            'url',
            'description',
        )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = (
            'id',
            'url',
            'department_title',
            'lead_employee',
        )


class BillableItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BillableItem
        fields = (
            'id',
            'url',
            'description',
            'bill_type',
            'department',
            'is_billed_overtime',
            'is_default',
        )


class BillableItemReadSerializer(BillableItemSerializer):
    bill_type = BillTypeSerializer()
    department = DepartmentSerializer()


class BillRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BillRate
        fields = (
            'id',
            'url',
            'rate',
            'billable_item',
            'overtime_bill_rate',
            'client',
            'project',
        )


class BillRateReadSerializer(BillRateSerializer):
    billable_item = BillableItemSerializer()


