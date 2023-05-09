from django.contrib import admin

from myblog.models import MyBlog, MyBlogPost, MyBlogPhotoPost


@admin.register(MyBlog)
class MyBlogAdmin(admin.ModelAdmin):
    pass
@admin.register(MyBlogPost)
class MyBlogPostAdmin(admin.ModelAdmin):
    pass
@admin.register(MyBlogPhotoPost)
class MyBlogPhotoAdmin(admin.ModelAdmin):
    pass