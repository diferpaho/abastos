from django.urls import path, include
from apps.factura.views import index
app_name='factura'
urlpatterns = [
    path('', index),
]
 