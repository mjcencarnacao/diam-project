from django.urls import path
from . import views

# URLConf
app_name = 'home'
urlpatterns = [
    path('', views.get_home_page),


]
