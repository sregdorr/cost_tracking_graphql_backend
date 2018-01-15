import uuid

from django.db.models import CharField, ForeignKey, DO_NOTHING, Model, UUIDField

from common.base_models import ActivatableModel


class Department(ActivatableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_title = CharField(max_length=20)
    lead_employee = ForeignKey('employees.Employee',
                               related_name='departments',
                               on_delete=DO_NOTHING,
                               null=True,
                               blank=True)

    def __str__(self):
        return self.department_title
