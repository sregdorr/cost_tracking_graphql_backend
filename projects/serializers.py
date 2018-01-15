from rest_framework import serializers

from projects import models
import clients.serializers as client_serializers


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectType
        fields = (
            'id',
            'url',
            'description'
        )


class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectStatus
        fields = (
            'id',
            'url',
            'status',
        )


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkOrder
        fields = (
            'id',
            'url',
            'limit',
            'is_active',
            'created_date',
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = (
            'id',
            'url',
            'project_name',
            'client',
            'lead_employee',
            'project_status',
            'office',
            'requires_afe',
            'work_order',
            'project_type',
            'is_active',
            'created_date',
        )


class ProjectReadSerializer(ProjectSerializer):
    # project_subsets = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='projectsubset-detail'
    # )
    client = client_serializers.ClientSerializer()
    work_order = serializers.StringRelatedField()
    project_type = ProjectTypeSerializer()


class ProjectSubsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectSubset
        fields = (
            'id',
            'url',
            'project_subset_name',
            'work_order',
            'project_manager',
            'project',
            'is_active',
            'created_date',
        )


class ProjectSubsetReadSerializer(ProjectSubsetSerializer):
    work_order = WorkOrderSerializer()
    project = ProjectSerializer()