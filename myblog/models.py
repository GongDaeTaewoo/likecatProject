from django.db import models

from likecatProject import settings


class MyBlog(models.Model):

    recommend = models.IntegerField(default=0)
    # 블로그 이름, 블로그에서 닉네임으로 활용
    blog_name = models.CharField(max_length=20,default="익명의 블로그")
    blog_intro= models.TextField(default="블로그 설명을 작성해주세요")
class MyBlogPost(models.Model):
    blog = models.ForeignKey(MyBlog, on_delete=models.CASCADE)
    author = models.CharField(max_length=25)
    subject_group = (('고양이','고양이'),('자유','자유'))
    subject = models.CharField(max_length=20, choices=subject_group)
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
    content = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
