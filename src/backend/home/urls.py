from django.urls import path
from . import views
from members import views as member_views

# URLConf
app_name = 'home'
urlpatterns = [
    path('', views.get_home_page, name='home_page'),
    path('top/', views.get_home_page, name='home_page'),
    path('details/<movie_id>', views.movie_details, name='movie-details'),
    path('like_movie/<int:pk>', views.like_movie, name="like-movie"),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('search', views.search_movies, name='movie-search'),
    path('evaluate/', views.get_eval, name='eval'),
    path('erase/', views.erase_comment, name='erase'),
    path('add_movie/<int:pk>', views.add_movie_to_watchlist, name="add-to-watchlist"),
    path('check_movie_seen/<int:pk>', views.check_movie_seen, name="seen_movie"),
]
