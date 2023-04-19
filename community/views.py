from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from community.forms import FreePostForm, PicturePostForm
from community.models import FreePost1, FreePicturePost


def home(request):
    return render(request, 'community/home.html')


def free(request):
    post_list = FreePost1.objects.all().order_by('-pub_date')
    context = {"post_list": post_list}
    return render(request, 'community/free.html', context=context)


def free_write(request):
    if request.method == "POST":
        form = FreePostForm(request.POST)
        if form.is_valid():
            # commit=False일 경우 db에 저장 x 하고 모델객체 만들어서 리턴
            # **의뜻 정확히 추가공부!
            # post = FreePost1(**form.cleaned_data)
            post = form.save(commit=False)
            # 로그인시스템만들면 익명 변경하기
            post.author = "익명"
            post.save()
        return redirect(post)
    else:
        form = FreePostForm()
    return render(request, 'community/writeForm.html', context={"form": form})


def free_detail(request, pk):
    post = get_object_or_404(FreePost1, pk=pk)
    context = {"post": post}
    return render(request, 'community/free_detail.html', context=context)


def free_delete(request, pk):
    if request.method == "POST":
        post = get_object_or_404(FreePost1, pk=pk)
        post.delete()
        return redirect('community:free_board')
    else:
        return render(request, 'community/free_delete_confirm.html')


def free_edit(request, pk):
    post = get_object_or_404(FreePost1, pk=pk)
    if request.method == "POST":
        form = FreePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect(post)
    else:
        form = FreePostForm(instance=post)
        return render(request, 'community/free_edit.html', {"form": form, "pk": pk})


class PictureListView(ListView):
    model = FreePicturePost
    template_name = 'community/picture_board.html'
    context_object_name = 'post_list'
    # 템플릿에 들어가는 컨텍스트 이름으로 기본은 object 또는 object_list임


picture_board = PictureListView.as_view()


class PictureCreateView(CreateView):
    model = FreePicturePost
    template_name = 'community/picture_write.html'
    context_object_name = 'form'
    form_class = PicturePostForm
    # detail뷰 작성시 거기로 넘겨주기로 바꿔야함
    # success_url = reverse_lazy('community:picture_board')
    def get_success_url(self):
        return reverse('community:picture_detail', args=[self.object.pk])

class PictureUpdateView(UpdateView):
    model = FreePicturePost
    template_name = 'community/picture_update.html'
    context_object_name = 'form'
    form_class = PicturePostForm
    success_url = reverse_lazy('community:picture_board')
    def get_success_url(self):
        return reverse('community:picture_detail', args=[self.object.pk])


class PictureDetailView(DetailView):
    model = FreePicturePost
    template_name = 'community/picture_detail.html'
    context_object_name = 'post'


class PictureDeleteView(DeleteView):
    model = FreePicturePost
    template_name = 'community/picture_delete_confirm.html'
    context_object_name = 'form'
    success_url = reverse_lazy('community:picture_board')


picture_update = PictureUpdateView.as_view()
picture_detail = PictureDetailView.as_view()
picture_write = PictureCreateView.as_view()
picture_delete = PictureDeleteView.as_view()

def my_page(request):
    return render(request,'community/mypage.html')