from django.db.models import Model, CharField


class TaskStatus(Model):
    description = CharField(max_length=50)

    class Meta:
        verbose_name = 'Task Status'
        verbose_name_plural = 'Task Statuses'

    def __str__(self):
        return self.description
