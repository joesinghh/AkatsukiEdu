from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display    = ('username', 'email', 'is_teacher', 'admin', 'staff','is_active')
    search_fields = ('username', 'email')
    readonly_fields  = ('id',)

    fieldsets = ()
    filter_horizontal = ()
    list_filter = ('is_teacher',)

admin.site.register(User, AccountAdmin)


