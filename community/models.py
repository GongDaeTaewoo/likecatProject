from django.db import models
from django.urls import reverse


class FreePost1(models.Model):
    author = models.CharField(max_length=25)
    subject = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        # detail뷰 만들면 args=[self.pk]reverse함수의 두번째인자로넣기
        return reverse('community:free_board')


class FreePicturePost(models.Model):
    author = models.CharField(max_length=25)
    subject = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    picture = models.ImageField(upload_to="picture/%Y/%m/%d/", blank=True)
    picture2 = models.ImageField(upload_to="picture/%Y/%m/%d/", blank=True)
    content = models.CharField(max_length=700)
    pub_date = models.DateTimeField(auto_now_add=True)
