from django.urls import path
from . import views

app_anme = 'Home'
urlpatterns = [
    path('', views.home, name='home'),
]