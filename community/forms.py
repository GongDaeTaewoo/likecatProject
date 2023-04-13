from django import forms


class FreeWriteForm(forms.Form):
    author = forms.CharField(max_length=25)
    title = forms.CharField(max_length=20)
    content = forms.CharField(max_length=500)
