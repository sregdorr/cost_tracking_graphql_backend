from django.db.models import CharField, Model

from api.models.base_models import ActivatableModel, CreateableModel


class BillType(Model, ActivatableModel, CreateableModel):
    description = CharField(max_length=20)

    def __str__(self):
        return self.description
