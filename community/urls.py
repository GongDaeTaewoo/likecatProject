from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.home, name='home'),
    path('free/', views.free, name='free_board'),
    path('free/write/', views.free_write, name='free_board_write')
]
