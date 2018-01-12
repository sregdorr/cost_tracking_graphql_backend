from django.contrib import admin

from projects import models


class ProjectSubsetInline(admin.StackedInline):
    model = models.ProjectSubset


class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectSubsetInline, )


admin.site.register(models.ProjectType)
admin.site.register(models.ProjectStatus)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.WorkOrder)