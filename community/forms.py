from django import forms

from community.models import FreePost1, FreePicturePost


# class FreeWriteForm(forms.Form):
#     author = forms.CharField(max_length=25)
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(max_length=500)

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost1
        fields = ['subject', 'title', 'content']
        widgets = {
            "subject": forms.TextInput(
                # attrs={
                #     "class":
                # }
            )
            , "title": forms.TextInput()
            , "content": forms.Textarea()

        }
        labels = {
            "subject": "주제",
            "title": "제목",
            "content": "내용",
        }


class PicturePostForm(forms.ModelForm):
    class Meta:
        model = FreePicturePost
        fields = ['subject', 'title', 'picture', 'picture2', 'content']
        widgets = {
            "subject": forms.TextInput(
                # attrs={
                #     "class":
                # }
            )
            , "title": forms.TextInput()
            , "content": forms.Textarea()

        }
        labels = {
            "subject": "주제",
            "title": "제목",
            "content": "내용",
            "picture": "사진1",
            "picture2": "사진2",
        }
