from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('study', views.study, name='study'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)