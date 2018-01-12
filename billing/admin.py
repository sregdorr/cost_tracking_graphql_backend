from django.contrib import admin

from billing import models


class BillRateInline(admin.TabularInline):
    model = models.BillRate


class BillableItemAdmin(admin.ModelAdmin):
    inlines = [
        BillRateInline
    ]


admin.site.register(models.BillType)
admin.site.register(models.BillableItem, BillableItemAdmin)
admin.site.register(models.Department)