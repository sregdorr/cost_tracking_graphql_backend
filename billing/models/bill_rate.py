import uuid

from django.db.models import ForeignKey, \
    DecimalField, \
    DO_NOTHING, Model, UUIDField

from common.base_models import ActivatableCreateableModel


class BillRate(ActivatableCreateableModel):
    # id = UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    rate = DecimalField(max_digits=6, decimal_places=2)
    billable_item = ForeignKey('BillableItem', related_name='bill_rates', on_delete=DO_NOTHING)
    overtime_rate = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    client = ForeignKey('clients.Client', related_name='bill_rates', on_delete=DO_NOTHING, null=True, blank=True)
    project = ForeignKey('projects.Project', related_name='bill_rates', on_delete=DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = 'Bill Rate'
        verbose_name_plural = 'Bill Rates'

    def __str__(self):
        return self.billable_item.description + ' - ' + str(self.rate)
