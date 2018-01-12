from django.contrib import admin

from invoicing import models

admin.site.register(models.Invoice)
admin.site.register(models.InvoiceStatus)
