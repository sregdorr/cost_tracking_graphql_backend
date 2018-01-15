import uuid

from django.db.models import CharField, Model, UUIDField

from common.base_models import ActivatableCreateableModel


class BillType(ActivatableCreateableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = CharField(max_length=20)

    class Meta:
        verbose_name = 'Bill Type'

    def __str__(self):
        return self.description
