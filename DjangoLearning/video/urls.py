from django.urls import path

from . import views

app_name = 'video'
urlpatterns = [
    path('index', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('account_setting', views.account_setting, name='account_setting'),
    path('bookmarks', views.bookmarks, name='bookmarks'),
    path('like_videos', views.like_videos, name='like_videos'),
]