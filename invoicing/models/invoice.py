import uuid

from django.db.models import CharField, ForeignKey, \
    DateField, DO_NOTHING, Model, UUIDField

from common.base_models import CreateableModel


class Invoice(CreateableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_number = CharField(max_length=20)
    from_date = DateField()
    to_date = DateField()
    invoice_status = ForeignKey('InvoiceStatus', related_name='invoices', on_delete=DO_NOTHING)

    def __str__(self):
        return self.invoice_number
