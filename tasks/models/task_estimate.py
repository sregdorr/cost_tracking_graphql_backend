from django.db.models import CharField, ForeignKey, \
    FloatField, \
    DO_NOTHING, Model

from common.base_models import ActivatableCreateableModel, ModifiableModel


class TaskEstimate(ActivatableCreateableModel):
    comment = CharField(max_length=50)
    task = ForeignKey('Task', related_name='task_estimates', on_delete=DO_NOTHING)
    bill_rate = ForeignKey('billing.BillRate', related_name='task_estimates', on_delete=DO_NOTHING)
    estimated_hours = FloatField()
    parent = ForeignKey(
        'self', related_name='modified_estimates',
        on_delete=DO_NOTHING, null=True, blank=True
    )

    class Meta:
        verbose_name = 'Task Estimate'

    def __str__(self):
        return str(self.estimated_hours) + '@' + str(self.bill_rate)
