from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'name', 'date_joined', 'last_login', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Follower)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'user')
    search_fields = ('follower', 'user')

@admin.register(UserPreferedScreenMode)
class ScreenModeAdmin(admin.ModelAdmin):
    list_display = ('user', 'mode')
    search_fields = ('user', 'mode')




admin.site.register(Account, AccountAdmin)
