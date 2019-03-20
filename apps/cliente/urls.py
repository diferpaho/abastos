from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


from apps.cliente.views import index, contacto, listaUsuario, crearUsuario, inicio, modificarUsuario, eliminarUsuario
from apps.cliente.views import entrar, menuadm, listaLocales, listaLocalesMapa, localCrear, localModificar, localEliminar
app_name='cliente'
urlpatterns = [
    path('mapa/', listaLocalesMapa.as_view(),name='index'),
    path('listalocales/', listaLocales.as_view(),name='listaLocales'),
    path('localcrear/', localCrear.as_view(),name='localCrear'),
    path('editarlocal/<int:pk>/', login_required(localModificar.as_view()), name='localModificar'),
    path('localeliminar/<int:pk>/', login_required(localEliminar.as_view()), name='localEliminar'),
    path('entrar/', entrar,name='entrar'),
    path('contacto/', contacto,name='contacto'),
    path('lista/', login_required(listaUsuario.as_view()),name='login_listar'),
    path('nuevo/', crearUsuario.as_view(),name='nuevo'),
    path('editar/<int:pk>/', login_required(modificarUsuario.as_view()), name='modificar'),
    path('eliminar/<int:pk>/', login_required(eliminarUsuario.as_view()), name='eliminar'),
    path('adm/', auth_views.LoginView.as_view(template_name="cliente/loginAdm.html"),name='entrarA'),
    path('menuadm/', login_required(menuadm) ,name='menuadm'),
    
]
 