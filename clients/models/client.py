from django.db.models import CharField, ForeignKey, \
    DO_NOTHING, Model

from common.base_models import ActivatableCreateableModel


class Client(ActivatableCreateableModel):
    client_name = CharField(max_length=50)
    address = CharField(max_length=50, null=True, blank=True)
    city = CharField(max_length=50, null=True, blank=True)
    state = CharField(max_length=50, null=True, blank=True)
    zip_code = CharField(max_length=50, null=True, blank=True)
    phone = CharField(max_length=50, null=True, blank=True)
    primary_contact = ForeignKey('Contact', related_name='clients', on_delete=DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.client_name
