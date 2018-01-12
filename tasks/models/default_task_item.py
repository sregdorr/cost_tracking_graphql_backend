from django.db.models import Model, CharField


class DefaultTaskItem(Model):
    description = CharField(max_length=50)

    class Meta:
        verbose_name = 'Default Task Item'

    def __str__(self):
        return self.description
