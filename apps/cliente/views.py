from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'cliente/index.html')

# Create your views here.
def contacto(request):
	return render(request, 'cliente/contacto.html')

def login(request):
	return render(request, 'cliente/login.html')

def inicio(request):
	return render(request, 'cliente/inicio.html')