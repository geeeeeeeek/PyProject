from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('<int:pk>/detail',views.DetailView.as_view(), name='detail'),
    path('comment',views.comment, name='comment')
]