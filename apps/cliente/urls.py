from django.urls import path, include
from apps.cliente.views import index, contacto, login, inicio

urlpatterns = [
    path('mapa/', index),
    path('contacto/', contacto),
    path('login/', login),
    path('home/', inicio),
]
 