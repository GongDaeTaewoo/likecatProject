from django.shortcuts import render, redirect

from community.forms import FreeWriteForm
from community.models import FreePost1


def home(request):
    return render(request, 'community/home.html')


def free(request):
    post_list = FreePost1.objects.all().order_by('-pub_date')
    context = {"post_list": post_list}
    return render(request, 'community/free.html', context=context)


def free_write(request):
    if request.method == "POST":
        form = FreeWriteForm(request.POST)
        if form.is_valid():
            # commit=False일 경우 db에 저장 x 하고 모델객체 만들어서 리턴
            # **의뜻 정확히 추가공부!
            post = FreePost1(**form.cleaned_data)
            post.save()
        return redirect(post)
    else:
        form = FreeWriteForm()
    return render(request, 'community/writeForm.html', context={"form": form})
