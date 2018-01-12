from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from employees import models


class EmployeeInLine(admin.StackedInline):
    model = models.Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "is_active",
        "is_staff",
        "last_login",
        "date_joined"
    )
    inlines = (EmployeeInLine,)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        # (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(models.Employee)
admin.site.register(models.Office)
