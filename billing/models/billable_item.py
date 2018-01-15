import uuid

from django.db.models import CharField, ForeignKey, \
    BooleanField, DO_NOTHING, Model, UUIDField

from common.base_models import ActivatableModel


class BillableItem(ActivatableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = CharField(max_length=50)
    bill_type = ForeignKey('BillType', related_name='billable_items', on_delete=DO_NOTHING)
    department = ForeignKey('Department', related_name='billable_items', on_delete=DO_NOTHING)
    is_billed_overtime = BooleanField()
    is_default = BooleanField()

    class Meta:
        verbose_name = 'Billable Item'

    def __str__(self):
        return self.description