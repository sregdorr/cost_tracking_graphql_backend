import uuid
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models import \
    CharField, ForeignKey, \
    IntegerField, DateField, \
    EmailField, ManyToManyField, OneToOneField, DO_NOTHING, Model, UUIDField

from django.contrib.auth.models import User

from common.base_models import ActivatableCreateableModel


class Employee(ActivatableCreateableModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    middle_initial = CharField(max_length=1)
    email = EmailField(max_length=50)
    cell_phone = CharField(max_length=20, null=True, blank=True)
    office_phone = CharField(max_length=20, null=True, blank=True)
    office_ext = IntegerField(null=True, blank=True)
    manager = ForeignKey('self', related_name='supervised_employees', on_delete=DO_NOTHING, null=True, blank=True)
    office = ForeignKey('Office', related_name='employees', on_delete=DO_NOTHING)
    current_week_start = DateField()
    positions = ManyToManyField('billing.BillRate')
    user = OneToOneField(User, on_delete=DO_NOTHING, unique=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


# have django automatically save an authentication token when adding a user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)