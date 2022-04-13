from django.urls import path
from . import views

# URLConf
app_name = 'home'
urlpatterns = [
    path('', views.get_home_page),
    path('login', views.get_login_page, name='login'),
    path('register', views.get_register_page, name='register'),
    path('details', views.get_details_page, name='details'),
]
