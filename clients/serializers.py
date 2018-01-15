from rest_framework import serializers

from clients import models
import employees.serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = (
            'id',
            'url',
            'first_name',
            'last_name',
            'company',
            'position',
            'office_phone',
            'cell_phone',
            'email',
        )


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class ClientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = (
            'id',
            'url',
            'client_name',
        )


class ClientReadSerializer(ClientSerializer):
    primary_contact = serializers.StringRelatedField()
    lead_employee = employees.serializers.EmployeeSerializer()
    user = serializers.StringRelatedField()