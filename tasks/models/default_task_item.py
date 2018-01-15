import uuid

from django.db.models import Model, CharField, UUIDField


class DefaultTaskItem(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = CharField(max_length=50)

    class Meta:
        verbose_name = 'Default Task Item'

    def __str__(self):
        return self.description
