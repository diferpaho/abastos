from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from apps.cliente.models import Cliente, Registrar
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.cliente.forms import ClienteForm, RegistrarForm
from django.urls import reverse_lazy
from apps.producto.models import Local
from apps.producto.forms import LocalForm


def index(request):
	return render(request, 'cliente/index.html')

def entrar(request):
	return render(request, 'cliente/loginEntrar.html')

# Create your views here.
def contacto(request):
	return render(request, 'cliente/contacto.html')

class listaUsuario(ListView):
	model= Registrar
	template_name= 'cliente/login.html'

class listaLocalesMapa(ListView):
	model= Local
	template_name= 'cliente/index.html'	

class listaLocales(ListView):
	model= Local
	template_name= 'cliente/listaLocales.html'

class localCrear(CreateView):
	model= Local
	form_class= LocalForm
	template_name='cliente/localCrear.html'
	success_url= reverse_lazy('cliente:listaLocales')

class localModificar(UpdateView):
	model= Local
	form_class= LocalForm
	template_name='cliente/localCrear.html'
	success_url= reverse_lazy('cliente:listaLocales')	

class localEliminar(DeleteView):
	model= Local
	template_name='cliente/localEliminar.html'
	success_url= reverse_lazy('cliente:listaLocales')			
	
class crearUsuario(CreateView):
	model=Registrar
	template_name='cliente/loginCrear.html'
	form_class= RegistrarForm
	second_form_class= ClienteForm  
	success_url = reverse_lazy('cliente:login_listar')

	def get_context_data(self, **kwargs):
		context = super(crearUsuario, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form']=self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2']= self.second_form_class(self.request.GET)
		return context	

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form= self.form_class(request.POST)
		form2=self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			login= form.save(commit=False)
			login.cliente=form2.save()
			login.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))



def inicio(request):
	return render(request, 'inicio.html')

def menuadm(request):
	return render(request, 'cliente/menuAdm.html')

class modificarUsuario(UpdateView):
	model = Registrar
	second_model= Cliente
	template_name= 'cliente/loginCrear.html'
	form_class= RegistrarForm
	second_form_class= ClienteForm
	success_url= reverse_lazy('cliente:login_listar')

	def get_context_data(self, **kwargs):
		context = super(modificarUsuario, self).get_context_data(**kwargs)
		pk= self.kwargs.get('pk',0)
		solicitud= self.model.objects.get(id=pk)
		cliente= self.second_model.objects.get(id=solicitud.cliente_id)
		if 'form' not in context:
			context['form']= self.form_class()
		if 'form2' not in context:
			context['form2']= self.second_form_class(instance=cliente)
		context['id']=pk
		return context	

	def post(self, request, *args, **kwargs):
		self.object= self.get_object
		id_solicitud= kwargs['pk']
		solicitud= self.model.objects.get(id=id_solicitud)
		cliente= self.second_model.objects.get(id=solicitud.cliente_id)
		form= self.form_class(request.POST,instance=solicitud)
		form2=self.second_form_class(request.POST, instance=cliente)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class eliminarUsuario(DeleteView):
	model= Registrar
	template_name='cliente/loginEliminar.html'
	success_url= reverse_lazy('cliente:login_listar')
	
