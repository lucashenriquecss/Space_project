from django.contrib import admin
from django.urls import path
from gallery.views import *
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id>/',imagem, name='imagem'),
]
