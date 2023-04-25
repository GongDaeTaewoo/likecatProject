from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/',views.register,name='register'),
    path('logout/', LogoutView.as_view(next_page='community:my_page'), name='logout'),
    path('mypage_p/', views.my_page_password, name='my_page_password'),
    path('mypage_inf/', views.my_page_inf_change, name='my_page_inf_change'),
]
app_name = 'accounts'
