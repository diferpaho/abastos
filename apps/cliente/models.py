from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model):
	nombre=  models.CharField(max_length=60)
	apellido=  models.CharField(max_length=60)
	fecha= models.DateField()
	email= models.EmailField()
	telefono= models.IntegerField()
	direccion= models.TextField()
	user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)

class Registrar(models.Model):
	cliente= models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	nombreUsuario= models.CharField(max_length=50)
	password= models.CharField(max_length=50)

