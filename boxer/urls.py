from django.urls import path
from . import views

app_name = 'boxer'
urlpatterns = [
    path('', views.boxer_info, name='boxer_info'),
   
]