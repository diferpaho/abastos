"""abastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.cliente.views import inicio, entrar
from django.contrib.auth import views as authViews
from django.contrib.auth.views import logout_then_login
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include('apps.cliente.urls')),
    path('factura/', include('apps.factura.urls')),
    path('producto/', include('apps.producto.urls')),
    path('', inicio,name='home'),
    path('accounts/login/', entrar,name='entrar'),
    path('logout/', logout_then_login,name='logout'),
    #path('reset/password_reset', PasswordResetView.as_view(), {'template_name':'registration/password_reset_form.html', 
    #    'email_template_name':'registration/password_reset_email.html'}, 
    #    name='password_reset'),
    #path('reset/password_reset_done', password_reset_done,{'template_name':'registration/password_reset_done.html'},
    #    name='password_reset_done'),
    #path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,{'template_name':'registration/password_reset_confirm.html'},
    #    name='password_reset_confirm'),
    #path('reset/done', password_reset_complete,{'template_name':'registration/password_reset_complete.html'},
    #    name='password_reset_complete'),

    
]
