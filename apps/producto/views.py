from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.producto.models import Local, Producto
from apps.producto.forms import LocalForm, ProductoForm


def index(request):
	return render(request, 'producto/index.html')

class productoLista(ListView):
	model= Producto
	template_name= 'producto/productoLista.html'

class productoCrear(CreateView):
	model=Producto
	template_name='producto/productoCrear.html'
	form_class= ProductoForm
	second_form_class= LocalForm
	success_url = reverse_lazy('producto:productoLista')

	def get_context_data(self, **kwargs):
		context = super(productoCrear, self).get_context_data(**kwargs)
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
			login.producto=form2.save()
			login.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))