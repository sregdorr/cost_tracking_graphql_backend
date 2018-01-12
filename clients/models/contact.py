from django.db.models import Model, CharField


class Contact(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50, null=True, blank=True)
    company = CharField(max_length=50, null=True, blank=True)
    position = CharField(max_length=50, null=True, blank=True)
    office_phone = CharField(max_length=50, null=True, blank=True)
    cell_phone = CharField(max_length=50, null=True, blank=True)
    email = CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name
