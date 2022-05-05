from django.urls import path
from . import views
from members import views as member_views

# URLConf
app_name = 'home'
urlpatterns = [
    path('', views.get_home_page, name= 'home_page'),
    path('details/<movie_id>', views.movie_details, name= 'movie-details'),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('register', views.get_register_page, name='register'),
]