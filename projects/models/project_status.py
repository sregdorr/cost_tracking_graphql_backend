from django.db.models import Model, CharField


class ProjectStatus(Model):
    status = CharField(max_length=50)

    class Meta:
        verbose_name = 'Project Status'
        verbose_name_plural = 'Project Statuses'

    def __str__(self):
        return self.status
