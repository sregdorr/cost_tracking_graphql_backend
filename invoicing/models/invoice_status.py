from django.db.models import CharField, Model

from common.base_models import CreateableModel


class InvoiceStatus(CreateableModel):
    status = CharField(max_length=20)

    class Meta:
        verbose_name = "Invoice Status"
        verbose_name_plural = 'Invoice Statuses'

    def __str__(self):
        return self.status
