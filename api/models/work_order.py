from django.db.models import CharField, DecimalField, Model

from api.models.base_models import ActivatableModel, CreateableModel


class WorkOrder(Model, ActivatableModel, CreateableModel):
    work_order_number = CharField(max_length=50)
    limit = DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.work_order_number
