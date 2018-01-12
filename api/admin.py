from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from api import models


class EmployeeInLine(admin.StackedInline):
    model = models.Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInLine, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(models.BillRate)
admin.site.register(models.BillType)
admin.site.register(models.BillableItem)
admin.site.register(models.Client)
admin.site.register(models.Contact)
admin.site.register(models.DefaultTaskItem)
admin.site.register(models.Department)
admin.site.register(models.Employee)
admin.site.register(models.Entry)
admin.site.register(models.EntryStatus)
admin.site.register(models.Invoice)
admin.site.register(models.InvoiceStatus)
admin.site.register(models.Office)
admin.site.register(models.ProjectType)
admin.site.register(models.ProjectStatus)
admin.site.register(models.Project)
admin.site.register(models.ProjectSubset)
admin.site.register(models.Task)
admin.site.register(models.TaskStatus)
admin.site.register(models.TaskEstimate)
admin.site.register(models.WorkOrder)
