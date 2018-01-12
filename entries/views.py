from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from common.mixins.view_mixins import MultiSerializerViewSetMixin
from entries.models import Entry, EntryStatus
from entries import serializers


class EntryStatusesViewSet(ModelViewSet):
    queryset = EntryStatus.objects.all()
    serializer_class = serializers.EntryStatusSerializer


class EntriesViewSet(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = serializers.EntrySerializer