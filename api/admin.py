from django.contrib import admin
from .models import Client, Project


class ClientAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
