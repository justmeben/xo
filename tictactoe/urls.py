from django.contrib import admin
from django.urls import path, include

from tictactoe import views

urlpatterns = [
    path('', views.GameGetView.as_view()),
    path('start/', views.GameStartView.as_view()),
    path('reset/', views.GameResetView.as_view()),
    path('move/', views.GameMoveView.as_view()),
]
