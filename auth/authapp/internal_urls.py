from django.contrib import admin
from django.urls import path, include

from authapp.internal_views import ValidateAuth

urlpatterns = [
    path('validate/', ValidateAuth.as_view()),
]
