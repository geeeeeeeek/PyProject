from django.urls import path

from . import views

app_name = 'myadmin'
urlpatterns = [
    path('index', views.index, name='index'),
]