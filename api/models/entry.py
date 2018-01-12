from django.db.models import Model, CharField, ForeignKey, \
    DateField, FloatField, BooleanField, DO_NOTHING, Model

from api.models.base_models import ActivatableModel, ModifiableModel, CreateableModel


class Entry(Model, ActivatableModel, CreateableModel, ModifiableModel):
    entry_date = DateField()
    employee = ForeignKey('Employee', related_name='entries', on_delete=DO_NOTHING)
    bill_rate = ForeignKey('BillRate', related_name='entries', on_delete=DO_NOTHING)
    task = ForeignKey('Task', related_name='entries', on_delete=DO_NOTHING)
    description = CharField(max_length=50)
    amount = FloatField()
    overtime = FloatField()
    invoice = ForeignKey(
        'Invoice', related_name='entries', on_delete=DO_NOTHING, null=True, blank=True)
    is_billable = BooleanField()
    office = ForeignKey('Office', related_name='entries', on_delete=DO_NOTHING)
    entry_status = ForeignKey('EntryStatus', related_name='entries', on_delete=DO_NOTHING)
    parent = ForeignKey('Entry', related_name='modified_edtries', on_delete=DO_NOTHING)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return str(self.entry_date) + ' - ' + self.description
