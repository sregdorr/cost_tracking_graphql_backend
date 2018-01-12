from django.contrib.auth.models import User

from django.db.models import Model, ForeignKey, \
    BooleanField, DateTimeField, DO_NOTHING


class ActivatableModel(object):
    is_active = BooleanField()


class CreateableModel(object):
    created_date = DateTimeField(auto_now_add=True)


class ModifiableModel(object):
    # You must implement a 'parent' field in the subclass
    pass
