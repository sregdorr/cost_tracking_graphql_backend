from django.contrib import admin

from entries import models

admin.site.register(models.Entry)
admin.site.register(models.EntryStatus)