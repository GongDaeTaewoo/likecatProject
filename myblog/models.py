from django.db import models

from likecatProject import settings


class MyBlog(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recommend = models.IntegerField(default=0)


class MyBlogPost(models.Model):
    blog = models.ForeignKey(MyBlog, on_delete=models.CASCADE)
    author = models.CharField(max_length=25)
    subject = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class MyBlogPhotoPost(models.Model):
    blog = models.ForeignKey(MyBlog, on_delete=models.CASCADE)
    author = models.CharField(max_length=25)
    subject = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='blog_photo/%Y/%m/%d/')
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class MyBlogPostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.OneToOneField(MyBlogPost, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class MyBlogPhotoPostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.OneToOneField(MyBlogPhotoPost, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
