import uuid

from django.db.models import Model, CharField, UUIDField


class EntryStatus(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = CharField(max_length=50)

    class Meta:
        verbose_name = "Entry Status"
        verbose_name_plural = "Entry Statuses"

    def __str__(self):
        return self.description