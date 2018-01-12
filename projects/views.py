from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from common.mixins.view_mixins import MultiSerializerViewSetMixin
from projects import serializers
from projects.models import ProjectType, ProjectStatus, Project, ProjectSubset


class ProjectTypesViewSet(ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = serializers.ProjectTypeSerializer


class ProjectStatusesViewSet(ModelViewSet):
    queryset = ProjectStatus.objects.all()
    serializer_class = serializers.ProjectStatusSerializer


class ProjectsViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    serializer_action_classes = {
        'list': serializers.ProjectReadSerializer,
        'retrieve': serializers.ProjectReadSerializer
    }


class ProjectSubsetsViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = ProjectSubset.objects.all()
    serializer_class = serializers.ProjectSubsetSerializer
    serializer_action_classes = {
        'list': serializers.ProjectSubsetReadSerializer,
        'retrieve': serializers.ProjectSubsetReadSerializer
    }