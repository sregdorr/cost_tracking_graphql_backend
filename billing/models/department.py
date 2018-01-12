from django.db.models import CharField, ForeignKey, DO_NOTHING, Model

from common.base_models import ActivatableModel


class Department(ActivatableModel):
    department_title = CharField(max_length=20)
    lead_employee = ForeignKey('employees.Employee',
                               related_name='departments',
                               on_delete=DO_NOTHING,
                               null=True,
                               blank=True)

    def __str__(self):
        return self.department_title
