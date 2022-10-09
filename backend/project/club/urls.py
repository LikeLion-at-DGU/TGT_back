from django.urls import URLPattern, path
from .views import *
from . import views

app_name = 'club'
urlpatterns = [
    path('', views.club_list_create),
]