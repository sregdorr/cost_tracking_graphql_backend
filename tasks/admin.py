from django.contrib import admin

from tasks import models

admin.site.register(models.DefaultTaskItem)
admin.site.register(models.Task)
admin.site.register(models.TaskStatus)
admin.site.register(models.TaskEstimate)