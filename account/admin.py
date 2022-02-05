from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active'
    readonly_fields = 'last_login', 'date_joined', 'is_active'
    ordering = '-date_joined',
    list_display_links = 'email', 'first_name', 'last_name'

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
