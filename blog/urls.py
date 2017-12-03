from django.contrib import admin
from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('study', views.study, name='study'),
]