import uuid
from django.db.models import UUIDField, CharField, ForeignKey, \
    DO_NOTHING, Model

from common.base_models import ActivatableCreateableModel, ActivatableCreateableModifiableModel


class Client(ActivatableCreateableModifiableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = CharField(max_length=50)
    address = CharField(max_length=50, null=True, blank=True)
    city = CharField(max_length=50, null=True, blank=True)
    state = CharField(max_length=50, null=True, blank=True)
    zip_code = CharField(max_length=50, null=True, blank=True)
    phone = CharField(max_length=50, null=True, blank=True)
    primary_contact = ForeignKey('Contact', related_name='clients', on_delete=DO_NOTHING, null=True, blank=True)
    lead_employee = ForeignKey('employees.Employee', related_name='clients', on_delete=DO_NOTHING)

    def __str__(self):
        return self.client_name
