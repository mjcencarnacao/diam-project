from django.urls import path
from . import views

# URLConf
app_name = 'members'
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('<int:user_id>/watchlist', views.get_watchlist_page, name='watchlist'),
    path('home/', views.home, name='home'),
    path('logout', views.logout_user, name='logout'),
    path('<int:user_id>/profile', views.get_profile_page, name='profile'),
    path('LoggedProfile/', views.login_user_profile, name='logged_profile_user')
]