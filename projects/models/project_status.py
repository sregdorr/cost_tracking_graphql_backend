import uuid

from django.db.models import Model, CharField, UUIDField


class ProjectStatus(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = CharField(max_length=50)

    class Meta:
        verbose_name = 'Project Status'
        verbose_name_plural = 'Project Statuses'

    def __str__(self):
        return self.status
