from django.contrib import admin

from myblog.models import MyBlog


@admin.register(MyBlog)
class MyBlogAdmin(admin.ModelAdmin):
    pass
