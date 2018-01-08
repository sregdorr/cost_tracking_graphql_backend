from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    zip = models.CharField(max_length=15, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.client_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_number = models.CharField(max_length=50, null=True, blank=True)
    budget = models.DecimalField(decimal_places=2, max_digits=11, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.project_name
