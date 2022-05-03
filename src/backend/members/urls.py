from django.urls import path
from . import views

# URLConf
app_name = 'members'
urlpatterns = [

    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home')

]