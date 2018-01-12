from django.db.models import CharField, ForeignKey, \
    DateField, FloatField, BooleanField, DO_NOTHING, Model

from common.base_models import ActivatableCreateableModel


class Entry(ActivatableCreateableModel):
    entry_date = DateField()
    employee = ForeignKey('employees.Employee', related_name='entries', on_delete=DO_NOTHING)
    bill_rate = ForeignKey('billing.BillRate', related_name='entries', on_delete=DO_NOTHING)
    task = ForeignKey('tasks.Task', related_name='entries', on_delete=DO_NOTHING)
    description = CharField(max_length=50)
    amount = FloatField()
    overtime = FloatField()
    invoice = ForeignKey(
        'invoicing.Invoice', related_name='entries', on_delete=DO_NOTHING, null=True, blank=True)
    is_billable = BooleanField()
    office = ForeignKey('employees.Office', related_name='entries', on_delete=DO_NOTHING)
    entry_status = ForeignKey('EntryStatus', related_name='entries', on_delete=DO_NOTHING)
    parent = ForeignKey('self', related_name='modified_edtries', on_delete=DO_NOTHING)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return str(self.entry_date) + ' - ' + self.description
