from django.db.models import CharField, ForeignKey, DO_NOTHING, Model

from api.models.base_models import ActivatableModel


class Department(Model, ActivatableModel):
    department_title = CharField(max_length=20)
    lead_employee = ForeignKey('Employee', related_name='departments', on_delete=DO_NOTHING)

    def __str__(self):
        return self.department_title