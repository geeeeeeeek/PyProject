from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('account_setting', views.account_setting, name='account_setting'),
    path('bookmarks', views.bookmarks, name='bookmarks'),
    path('like_videos', views.like_videos, name='like_videos'),
]
