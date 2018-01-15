import uuid

from django.db.models import Model, CharField, UUIDField


class ProjectType(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = CharField(max_length=50)

    class Meta:
        verbose_name = 'Project Type'

    def __str__(self):
        return self.description
