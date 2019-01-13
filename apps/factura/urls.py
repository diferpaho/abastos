from django.urls import path, include
from apps.factura.views import index

urlpatterns = [
    path('', index),
]
 