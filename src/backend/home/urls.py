from django.urls import path
from . import views
from members import views as member_views

# URLConf
app_name = 'home'
urlpatterns = [
    path('top/', views.get_home_page, name= 'home_page'),
    path('details/<movie_id>', views.movie_details, name= 'movie-details'),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('register', views.get_register_page, name='register'),
    path('<int:user_id>/profile', views.get_profile_page, name='profile'),
    path('search', views.search_movies, name='movie-search'),
    path('evaluate/', views.get_eval, name= 'eval'),
]