from django.db.models import CharField, Model

from api.models.base_models import CreateableModel


class InvoiceStatus(Model, CreateableModel):
    status = CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Invoice Statuses'

    def __str__(self):
        return self.status
