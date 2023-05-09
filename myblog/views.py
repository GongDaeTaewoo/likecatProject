from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from accounts.models import MyUser
from likecatProject import settings
from myblog.forms import BlogCreateForm, BlogFreePostForm, BlogFreePhotoForm
from myblog.models import MyBlogPost, MyBlog, MyBlogPhotoPost


def home(request):
    user_list = MyUser.objects.all().order_by('-blog__recommend').filter(blog__recommend__isnull=False)
    # blog_list=MyBlog.objects.all().order_by('-recommend')

    if request.user.is_authenticated:
        my_blog = request.user.blog
        return render(request, 'myblog/home.html', {'my_blog': my_blog,'user_list':user_list})
    else:
        my_blog=False
        return render(request, 'myblog/home.html',{'my_blog':my_blog,'user_list':user_list })



def myblog(request, userid):
    user = get_object_or_404(get_user_model(), username=userid)
    blog = user.blog
    return render(request, 'myblog/myblog.html', {'blog': blog, 'blog_user': user})


def blog_create(request, userid):
    user = get_object_or_404(get_user_model(), username=userid)
    if request.method == "POST":
        blog = MyBlog()
        blog.recommend = 0
        blog.blog_name = request.POST.get('name')
        blog.blog_intro = request.POST.get('intro')
        blog.save()
        user.blog = blog
        if not user.avatar:
            user.avatar = request.POST.get('avatar')
        user.save()

        return redirect('myblog:myblog', userid=userid)
    else:
        form = BlogCreateForm()
        return render(request, 'myblog/blog_create.html', {'form': form})


def blog_free(request, userid):
    user = get_object_or_404(get_user_model(), username=userid)
    post_list = MyBlogPost.objects.all().filter(blog=user.blog)
    return render(request, 'myblog/blog_free.html', {'post_list': post_list, 'blog_user': user})


def blog_free_detail(request, userid, pk):
    post = get_object_or_404(MyBlogPost, pk=pk)
    return render(request, 'myblog/blog_free_detail.html', {'post': post})


def blog_free_write(request, userid):
    user = get_object_or_404(get_user_model(), username=userid)
    if request.method == "POST":
        form = BlogFreePostForm(request.POST)
        post = form.save(commit=False)
        post.blog = user.blog
        post.author = user.username
        post.save()
        return redirect('myblog:blog_free_detail', userid=userid,pk=post.pk)
    else:

        form = BlogFreePostForm()
        return render(request, 'myblog/blog.free_write.html', {'form': form})


def blog_free_edit(request, userid, pk):
    post = get_object_or_404(MyBlogPost, pk=pk)
    if request.method == "POST":
        form = BlogFreePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('myblog:blog_free_detail', pk=pk, userid=userid)
    else:
        form = BlogFreePostForm(instance=post)
        return render(request, 'myblog/blog_free_edit.html', {'form': form})


def blog_free_delete(request, userid, pk):
    post = get_object_or_404(MyBlogPost, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('myblog:blog_free_board',userid=userid)
    else:
        return render(request, 'myblog/blog_free_delete.html',{'post':post})


def blog_photo(request, userid):
    user = get_object_or_404(get_user_model(), username=userid)
    post_list = MyBlogPhotoPost.objects.all().order_by('-pub_date').filter(blog=user.blog)
    return render(request, 'myblog/blog_photo.html', {'post_list': post_list})


def blog_photo_detail(request, userid, pk):
    post = get_object_or_404(MyBlogPhotoPost, pk=pk)
    return render(request, 'myblog/blog_photo_detail.html', {'post': post})


def blog_photo_write(request, userid):
    user = get_object_or_404(get_user_model(), username=userid)

    if request.method == "POST":
        form = BlogFreePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = user.blog
            post.author = user.username
            post.save()
            return redirect('myblog:blog_photo_detail', pk=post.pk,userid=userid)
    else:
        form = BlogFreePhotoForm()
        return render(request, 'myblog/blog_photo_write.html', {'form': form,'user':user})


def blog_photo_edit(request, userid, pk):
    post = get_object_or_404(MyBlogPhotoPost,pk=pk)
    if request.method == "POST":
        form = BlogFreePhotoForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('myblog:blog_photo_detail', userid=userid,pk=pk)

    else:
        form = BlogFreePhotoForm(instance=post)
        return render(request,'myblog/blog_photo_edit.html',{'form':form})


def blog_photo_delete(request, userid, pk):
    if request.method == "POST":
        post = get_object_or_404(MyBlogPhotoPost,pk=pk)
        post.delete()
        return redirect('myblog:blog_photo_board',userid=userid)
    else:
        return render(request,'myblog/blog_photo_delete.html')

def blog_recommend(request,userid):
    user = get_object_or_404(get_user_model(),username=userid)
    blog = user.blog
    blog.recommend+=1
    blog.save()
    return redirect('myblog:myblog', userid=userid)
