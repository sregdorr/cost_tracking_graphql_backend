from rest_framework import serializers
from entries.models import EntryStatus, Entry


class EntryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryStatus
        fields = (
            'id',
            'url',
            'description',
        )


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'id',
            'url',
            'entry_date',
            'bill_rate',
            'task',
            'description',
            'amount',
            'overtime',
            'invoice',
            'is_billable',
            'office',
            'created_date',
            'entry_status',
            'parent',
            'is_active',
            'user',
        )