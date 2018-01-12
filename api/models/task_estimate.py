from django.db.models import CharField, ForeignKey, \
    FloatField, \
    DO_NOTHING, Model

from api.models.base_models import ActivatableModel, CreateableModel, ModifiableModel


class TaskEstimate(Model, ActivatableModel, CreateableModel, ModifiableModel):
    comment = CharField(max_length=50)
    task = ForeignKey('Task', related_name='task_estimates', on_delete=DO_NOTHING)
    bill_rate = ForeignKey('BillRate', related_name='task_estimates', on_delete=DO_NOTHING)
    estimated_hours = FloatField()
    parent = ForeignKey(
        'TaskEstimate', related_name='modified_estimates',
        on_delete=DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return str(self.estimated_hours) + '@' + str(self.bill_rate)
