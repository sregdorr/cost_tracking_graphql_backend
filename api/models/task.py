from django.db.models import CharField, ForeignKey, \
    DateField, DO_NOTHING, Model

from api.models.base_models import ActivatableModel, CreateableModel


class Task(Model, ActivatableModel, CreateableModel):
    description = CharField(max_length=50)
    p6_task_id = CharField(max_length=50, null=True, blank=True)
    project_subset = ForeignKey('ProjectSubset', related_name='tasks', on_delete=DO_NOTHING)
    start_date = DateField()
    end_date = DateField()
    task_status = ForeignKey('TaskStatus', related_name='tasks', on_delete=DO_NOTHING)

    def __str__(self):
        return self.description
