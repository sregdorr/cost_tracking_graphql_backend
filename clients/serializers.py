from rest_framework import serializers

from clients import models


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
        fields = (
            'id',
            'url',
            'client_name',
            'address',
            'city',
            'state',
            'zip_code',
            'phone',
            'primary_contact',
        )


class ClientReadSerializer(ClientSerializer):
    primary_contact = serializers.StringRelatedField()