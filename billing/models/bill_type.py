from django.db.models import CharField, Model

from common.base_models import ActivatableCreateableModel


class BillType(ActivatableCreateableModel):
    description = CharField(max_length=20)

    class Meta:
        verbose_name = 'Bill Type'

    def __str__(self):
        return self.description
