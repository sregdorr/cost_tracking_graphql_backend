from django.db.models import CharField, ForeignKey, \
    BooleanField, DateTimeField, DO_NOTHING, Model

from common.base_models import ActivatableCreateableModel


class ProjectSubset(ActivatableCreateableModel):
    project_subset_name = CharField(max_length=100)
    work_order = ForeignKey(
        'WorkOrder', related_name='project_subsets', on_delete=DO_NOTHING, null=True, blank=True
    )
    project_manager = ForeignKey(
        'clients.Contact', related_name='project_subsets', on_delete=DO_NOTHING, null=True, blank=True
    )
    project = ForeignKey('Project', related_name='project_subsets', on_delete=DO_NOTHING)

    class Meta:
        verbose_name = 'Project Subset'

    def __str__(self):
        return self.project_subset_name
