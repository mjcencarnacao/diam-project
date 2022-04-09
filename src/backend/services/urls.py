from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('getTopMovies/', views.request_top_movies)
]
