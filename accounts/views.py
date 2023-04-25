from django.contrib import messages
from django.contrib.auth import login, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from accounts.forms import MyUserCreationForm, MyUserChangeForm


def register(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('community:home')
    else:
        form = MyUserCreationForm()
    return render(request, 'accounts/register.html', {"form": form})


def my_page_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            #이거 넣어줘야 로그인 다시안해도됨
            update_session_auth_hash(request, user)
            return redirect('community:my_page')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'community/mypage_password.html', {'form': form})


def my_page_inf_change(request):
    if request.method == "POST":
        form = MyUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('community:my_page')
    else:
        form = MyUserChangeForm(instance=request.user)
        return render(request, 'community/mypage_inf_change.html', {'form': form})
