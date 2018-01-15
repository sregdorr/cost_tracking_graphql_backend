import uuid

from django.db.models import \
    CharField, Model, UUIDField

from common.base_models import ActivatableCreateableModel


class Office(ActivatableCreateableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = CharField(max_length=50)
    address = CharField(max_length=50, null=True, blank=True)
    city = CharField(max_length=50, null=True, blank=True)
    state = CharField(max_length=50, null=True, blank=True)
    zip_code = CharField(max_length=50, null=True, blank=True)
    phone = CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.description
