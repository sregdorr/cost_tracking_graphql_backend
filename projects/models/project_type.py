from django.db.models import Model, CharField


class ProjectType(Model):
    description = CharField(max_length=50)

    class Meta:
        verbose_name = 'Project Type'

    def __str__(self):
        return self.description
