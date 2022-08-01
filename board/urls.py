from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('free_board_list/', views.free_board_list, name='free_board_list'),
    path('board_write/', views.board_write, name='board_write'),
    path('free_board_detail/<int:pk>/', views.free_board_detail, name='free_board_detail'),
    path('free_board_detail/<int:pk>/delete', views.free_board_delete, name='free_board_delete'),
    path('free_board_detail/<int:pk>/update', views.free_board_update, name='free_board_update'),
]