from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from tasks import models
from tasks import serializers


class DefaultTasksViewSet(ModelViewSet):
    queryset = models.DefaultTaskItem.objects.all()
    serializer_class = serializers.DefaultTaskSerializer


class TasksStatusesViewSet(ModelViewSet):
    queryset = models.TaskStatus.objects.all()
    serializer_class = serializers.TaskStatusSerializer


class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskEstimateViewSet(ModelViewSet):
    queryset = models.TaskEstimate.objects.all()
    serializer_class = serializers.TaskEstimateSerializer
