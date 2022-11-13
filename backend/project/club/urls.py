from django.urls import URLPattern, path
from .views import *
from . import views

app_name = 'club'
urlpatterns = [
    path('', views.club_list_create),
    path('<str:club_id>', club_detail, name='club_detail'),
    path('<str:club_id>/post', club_post_create, name='club_post'),
    path('<str:club_id>/post/<str:post_id>', club_post_detail, name='club_post_detail'),
    path('todolist',todo_list,name='todo_list'),
    path('todolist/<str:pk>/',todolist_detail,name="todolist_detail"),
]