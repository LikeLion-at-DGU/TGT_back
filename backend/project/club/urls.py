from django.urls import URLPattern, path
from .views import *
from . import views

app_name = 'club'
urlpatterns = [
    path('', views.club_list_create),
    path('todolist',todolist,name='list'),
    path('create/',todocreate, name='create'),
    path('update/<str:pk>/',todoupdate,name="update"),
    path('delete/<str:pk>/',tododelete, name='delete')
]