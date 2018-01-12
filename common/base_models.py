from django.contrib.auth.models import User

from django.db.models import Model, ForeignKey, \
    BooleanField, DateTimeField, DO_NOTHING


class ActivatableModel(Model):
    is_active = BooleanField(default=True)

    class Meta:
        abstract = True


class CreateableModel(Model):
    created_date = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ActivatableCreateableModel(Model):
    is_active = BooleanField(default=True)
    created_date = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ModifiableModel(Model):
    # You must implement a 'parent' field in the subclass
    pass

    class Meta:
        abstract = True