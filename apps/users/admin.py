from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('name', 'last_name', 'dni', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'last_name', 'dni', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'name', 'last_name', 'dni')
    ordering = ('username',)

admin.site.register(User, UserAdmin)