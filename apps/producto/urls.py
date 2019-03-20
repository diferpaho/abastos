from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from apps.producto.views import index, productoCrear, productoLista

app_name='producto'
urlpatterns = [
    path('index/', index,name='index'),
    path('productolista/', productoLista.as_view(),name='productoLista'),
    path('productocrear/', productoCrear.as_view(),name='productoCrear'),
   
]
 