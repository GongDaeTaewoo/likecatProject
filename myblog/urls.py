from django.urls import path

from myblog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:userid>/', views.myblog, name='myblog'),
    path('<str:userid>/create/', views.blog_create, name='blog_create'),
    path('<str:userid>/free/', views.blog_free, name='blog_free_board'),
    path('<str:userid>/photo/', views.blog_photo, name='blog_photo_board'),
    path('<str:userid>/free/write/', views.blog_free_write, name='blog_free_write'),
    path('<str:userid>/photo/write/', views.blog_photo_write, name='blog_photo_write'),
    path('<str:userid>/free/<int:pk>/', views.blog_free_detail, name='blog_free_detail'),
    path('<str:userid>/photo/<int:pk>/', views.blog_photo_detail, name='blog_photo_detail'),
    path('<str:userid>/free/<int:pk>/edit/', views.blog_free_edit, name='blog_free_edit'),
    path('<str:userid>/photo/<int:pk>/edit/', views.blog_photo_edit, name='blog_photo_edit'),
    path('<str:userid>/free/<int:pk>/delete/', views.blog_free_delete, name='blog_free_delete'),
    path('<str:userid>/photo/<int:pk>/delete/', views.blog_photo_delete, name='blog_photo_delete'),
    path('<str:userid>/blog_recommend/',views.blog_recommend,name='blog_recommend')
]
app_name = 'myblog'
