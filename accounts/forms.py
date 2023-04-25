from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'age', 'univ','job_group', 'job', 'gender']
        fields_classes = {"username": UsernameField}
        widgets = {
            'age': forms.NumberInput()
        }
        labels = {
            "age": "나이",
            "univ": "대학",
            "job_group": "직업군",
            "job": "직업",
            "gender": "성별"
        }


class MyUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()

        fields = ['last_name', 'first_name', 'age', 'univ', 'job_group', 'job', 'gender', 'email', ]
        widgets = {
            'age': forms.NumberInput()
        }
        labels = {
            "age": "나이",
            "univ": "대학",
            "job_group": "직업군",
            "job": "직업",
            "gender": "성별"
        }
