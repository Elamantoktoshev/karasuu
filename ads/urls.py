from django.contrib import admin
# from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import Karasu

urlpatterns = [
    path('karasu/', views.Karasu)
]
