from rest_framework import serializers
from invoicing.models import InvoiceStatus, Invoice


class InvoiceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceStatus
        fields = (
            'id',
            'url',
            'status'
        )


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'id',
            'url',
            'invoice_number',
            'from_date',
            'to_date',
            'invoice_status',
            'created_date',
            'entries'
        )


class InvoiceReadSerializer(InvoiceSerializer):
    entries = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='entry-detail'
    )
    invoice_status = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='invoice-detail'
    )