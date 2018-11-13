from django.urls import path

from . import views

app_name = 'video'
urlpatterns = [
    path('index', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]