# Generated by Django 4.2 on 2023-06-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_remove_myblog_bloguser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblogphotopostcomment',
            name='content',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myblogpost',
            name='subject',
            field=models.CharField(choices=[('고양이', '고양이'), ('자유', '자유')], max_length=20),
        ),
    ]