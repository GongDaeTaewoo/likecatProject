from django import forms

from myblog.models import MyBlogPost, MyBlogPhotoPost


class BlogCreateForm(forms.Form):
    name = forms.CharField(max_length=20, label="블로그 이름")
    intro = forms.CharField(max_length=50, label="블로그 설명")


class BlogFreePostForm(forms.ModelForm):
    class Meta:
        model = MyBlogPost
        fields = ['subject', 'title', 'content']
        labels = {
            'subject': "주제",
            "title": "제목",
            "content": "내용",
        }
        widgets = {
            'content': forms.Textarea()
        }


class BlogFreePhotoForm(forms.ModelForm):
    class Meta:
        model = MyBlogPhotoPost
        fields = ['subject', 'title', 'content', 'photo']
        labels = {
            'subject': "주제",
            'title': "제목",
            'content': "간단한 내용",
            'photo': "사진",
        }
