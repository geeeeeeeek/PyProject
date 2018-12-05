from django.urls import path
from . import views

app_name = 'video'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('detail', views.detail, name='detail'),
    path('search_result', views.SearchListView.as_view(), name='search_result'),
    path('add_video', views.add_video, name='add_video'),
]