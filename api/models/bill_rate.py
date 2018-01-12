from django.db.models import ForeignKey, \
    DecimalField, \
    DO_NOTHING, Model

from api.models.base_models import ActivatableModel, CreateableModel


class BillRate(Model, ActivatableModel, CreateableModel):
    rate = DecimalField(max_digits=6, decimal_places=2)
    billable_item = ForeignKey('BillableItem', related_name='bill_rates', on_delete=DO_NOTHING)
    overtime_bill_rate = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    client = ForeignKey('Client', related_name='bill_rates', on_delete=DO_NOTHING, null=True, blank=True)
    project = ForeignKey('Project', related_name='bill_rates', on_delete=DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = 'Bill Rate'
        verbose_name_plural = 'Bill Rates'

    def __str__(self):
        return self.rate
