from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.home, name='home'),
    path('free/', views.free, name='free_board'),
    path('free/write/', views.free_write, name='free_board_write'),
    path('free/<int:pk>/', views.free_detail, name='free_board_detail'),
    path('free/<int:pk>/edit/', views.free_edit, name='free_board_edit'),
    path('free/<int:pk>/delete/', views.free_delete, name='free_board_delete'),
    path('picture/', views.picture_board, name='picture_board'),
    path('picture/write/', views.picture_write, name='picture_board_write'),
    path('picture/<int:pk>/', views.picture_detail, name='picture_detail'),
    path('picture/<int:pk>/edit', views.picture_update, name='picture_edit'),
    path('picture/<int:pk>/delete', views.picture_delete, name='picture_delete'),
    path('mypage/', views.my_page, name='my_page'),


]
