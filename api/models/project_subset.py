from django.db.models import CharField, ForeignKey, \
    DO_NOTHING, Model

from api.models.base_models import ActivatableModel, CreateableModel


class ProjectSubset(Model, ActivatableModel, CreateableModel):
    project_subset_name = CharField(max_length=100)
    work_order = ForeignKey(
        'WorkOrder', related_name='project_subsets', on_delete=DO_NOTHING, null=True, blank=True
    )
    project_manager = ForeignKey(
        'Contact', related_name='project_subsets', on_delete=DO_NOTHING, null=True, blank=True
    )
    project = ForeignKey('Project', related_name='project_subsets', on_delete=DO_NOTHING)

    def __str__(self):
        return self.project_subset_name
