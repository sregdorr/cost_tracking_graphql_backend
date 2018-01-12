from django.db.models import CharField, ForeignKey, \
    BooleanField, DO_NOTHING, Model

from common.base_models import ActivatableModel


class BillableItem(ActivatableModel):
    description = CharField(max_length=50)
    bill_type = ForeignKey('BillType', related_name='billable_items', on_delete=DO_NOTHING)
    department = ForeignKey('Department', related_name='billable_items', on_delete=DO_NOTHING)
    is_billed_overtime = BooleanField()
    is_default = BooleanField()

    class Meta:
        verbose_name = 'Billable Item'

    def __str__(self):
        return self.description