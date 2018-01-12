from django.db.models import Model, CharField


class EntryStatus(Model):
    description = CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Entry Statuses"

    def __str__(self):
        return self.description