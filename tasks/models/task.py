import uuid

from django.db.models import CharField, ForeignKey, \
    DateField, DO_NOTHING, Model, UUIDField

from common.base_models import ActivatableCreateableModel


class Task(ActivatableCreateableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = CharField(max_length=50)
    p6_task_id = CharField(max_length=50, null=True, blank=True)
    project_subset = ForeignKey('projects.ProjectSubset', related_name='tasks', on_delete=DO_NOTHING)
    start_date = DateField()
    end_date = DateField()
    task_status = ForeignKey('TaskStatus', related_name='tasks', on_delete=DO_NOTHING)

    def __str__(self):
        return self.project_subset.project_subset_name + ' - ' + self.description
