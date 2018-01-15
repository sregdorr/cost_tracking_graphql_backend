import uuid

from django.db.models import CharField, DecimalField, Model, BooleanField, DateTimeField, UUIDField

from common.base_models import ActivatableCreateableModel


class WorkOrder(ActivatableCreateableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    work_order_number = CharField(max_length=50)
    limit = DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Work Order'

    def __str__(self):
        return self.work_order_number
