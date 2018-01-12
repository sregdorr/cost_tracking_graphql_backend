from django.db.models import CharField, ForeignKey, \
    BooleanField, DO_NOTHING, Model

from api.models.base_models import ActivatableModel, CreateableModel


class Project(Model, ActivatableModel, CreateableModel):
    project_name = CharField(max_length=100)
    client = ForeignKey('Client', related_name='projects', on_delete=DO_NOTHING)
    lead_employee = ForeignKey('Employee', related_name='projects', on_delete=DO_NOTHING)
    project_status = ForeignKey('ProjectStatus', related_name='projects', on_delete=DO_NOTHING)
    office = ForeignKey('Office', related_name='projects', on_delete=DO_NOTHING)
    requires_afe = BooleanField()
    work_order = ForeignKey('WorkOrder', related_name='projects', on_delete=DO_NOTHING)
    project_type = ForeignKey('ProjectType', related_name='projects', on_delete=DO_NOTHING)

    def __str__(self):
        return self.project_name
