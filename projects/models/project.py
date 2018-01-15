import uuid

from django.db.models import CharField, ForeignKey, \
    BooleanField, DateTimeField, DO_NOTHING, Model, UUIDField

from common.base_models import ActivatableCreateableModel


class Project(ActivatableCreateableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = CharField(max_length=100)
    client = ForeignKey('clients.Client', related_name='projects', on_delete=DO_NOTHING)
    lead_employee = ForeignKey('employees.Employee', related_name='projects', on_delete=DO_NOTHING)
    project_status = ForeignKey('ProjectStatus', related_name='projects', on_delete=DO_NOTHING)
    office = ForeignKey('employees.Office', related_name='projects', on_delete=DO_NOTHING)
    requires_afe = BooleanField()
    work_order = ForeignKey('WorkOrder', related_name='projects', on_delete=DO_NOTHING)
    project_type = ForeignKey('ProjectType', related_name='projects', on_delete=DO_NOTHING)

    def __str__(self):
        return self.project_name
