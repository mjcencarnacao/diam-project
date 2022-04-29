from django.urls import path
from . import views

# URLConf
app_name = 'home'
urlpatterns = [
    path('', views.get_home_page),
    path('details/<movie_id>', views.movie_details, name= 'movie-details')
]