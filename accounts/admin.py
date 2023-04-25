from django.contrib import admin

from accounts.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass