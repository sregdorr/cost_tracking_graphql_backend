import uuid

from django.db.models import CharField, Model, UUIDField

from common.base_models import CreateableModel


class InvoiceStatus(CreateableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = CharField(max_length=20)

    class Meta:
        verbose_name = "Invoice Status"
        verbose_name_plural = 'Invoice Statuses'

    def __str__(self):
        return self.status
