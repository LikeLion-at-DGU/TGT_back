from django.urls import URLPattern, path
from .views import *
from . import views

app_name = 'club'
urlpatterns = [
    path('', views.club_list_create),
    path('todolist',todo_list,name='todo_list'),
    path('todolist/<str:pk>/',todolist_detail,name="todolist_detail"),
]