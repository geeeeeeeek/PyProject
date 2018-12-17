from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('settings', views.settings, name='settings'),
    path('account_setting', views.account_setting, name='account_setting'),
    path('bookmarks', views.bookmarks, name='bookmarks'),
    path('like_videos', views.like_videos, name='like_videos'),

]
