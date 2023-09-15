from django.contrib.auth.models import AbstractUser
from django.db import models

from myblog.models import MyBlog


class MyUser(AbstractUser):
    avatar = models.ImageField(blank=True)
    age = models.IntegerField(blank=True, null=True)
    univ = models.CharField(max_length=15, blank=True)
    job = models.CharField(max_length=20, blank=True)
    blog = models.OneToOneField(MyBlog, on_delete=models.CASCADE, null=True)

    # 한국 고용직업분류2018에 나온 직업군 대분류
    # 첫번째는 db에저장 user.~하면 나옴 두번째는 선택할때 보이는것
    job_group_choices = (('경영,사무,금융,보험직', '경영,사무,금융,보험직')
                         , ('연구,공학,기술직', '연구,공학,기술직')
                         , ('교육,법률,사회복지,경찰,소방직 및 군인', '교육,법률,사회복지,경찰,소방직 및 군인')
                         , ('보건,의료직', '보건,의료직')
                         , ('예술,디자인,방송,스포츠직', '예술,디자인,방송,스포츠직')
                         , ('미용,경비,청소직', '미용,경비,청소직')
                         , ('영업등', '영업,판매,운전,운송직')
                         , ('영업,판매,운전,운송직', '건설,채굴직')
                         , ('설치,정비,생산직', '설치,정비,생산직')
                         , ('농립어업직', '농립어업직')
                         , ('기타', '기타'))
    job_group = models.CharField(max_length=30, default="기타", choices=job_group_choices)
    gender_choices = (('남성', '님성'), ('여성', '여성'))
    gender = models.CharField(max_length=7, choices=gender_choices)

