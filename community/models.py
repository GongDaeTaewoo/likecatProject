from django.db import models
from django.urls import reverse


class FreePost1(models.Model):
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        # detail뷰 만들면 args=[self.pk]reverse함수의 두번째인자로넣기
        return reverse('community:free_board')