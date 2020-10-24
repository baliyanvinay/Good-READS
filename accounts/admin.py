from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class CustomUserAdmin(UserAdmin):
    model = Account
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_author', 'picture')}),)
    list_display = ('first_name', 'last_name', 'username', 'is_author')


admin.site.register(Account, CustomUserAdmin)
