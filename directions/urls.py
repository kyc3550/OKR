from django.urls import path
from . import views

app_name = 'directions'
urlpatterns = [
    path('', views.directions, name='directions'),
   
]