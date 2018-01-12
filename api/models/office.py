from django.db.models import \
    CharField, Model

from api.models.base_models import ActivatableModel, CreateableModel


class Office(Model, ActivatableModel, CreateableModel):
    description = CharField(max_length=50)
    address = CharField(max_length=50, null=True, blank=True)
    city = CharField(max_length=50, null=True, blank=True)
    state = CharField(max_length=50, null=True, blank=True)
    zip_code = CharField(max_length=50, null=True, blank=True)
    phone = CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.description
