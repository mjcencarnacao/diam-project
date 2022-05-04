from django.urls import path
from . import views

# URLConf
app_name = 'members'
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('profile', views.get_profile_page, name='profile'),
    path('logout', views.logout_user, name='logout'),
]