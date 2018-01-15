from rest_framework import serializers

from tasks import models


class DefaultTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DefaultTaskItem
        fields = (
            'id',
            'url',
            'description'
        )


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskStatus
        fields = (
            'id',
            'url',
            'description'
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = (
            'id',
            'url',
            'description',
            'p6_task_id',
            'project_subset',
            'start_date',
            'end_date',
            'task_status',
        )


class TaskEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskEstimate
        fields = (
            'id',
            'url',
            'comment',
            'task',
            'bill_rate',
            'estimated_hours',
            'parent',
        )
