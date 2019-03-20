from django.db import models

# Create your models here.
class Local(models.Model):
	nombre=  models.CharField(max_length=50)
	ubicacion= models.TextField()
	administrador= models.CharField(max_length=50)

	def _str_(self):
		return '{}'.format(self.nombre)

class Producto(models.Model):
	nombre=  models.CharField(max_length=50)
	descripcion=  models.TextField()
	precio=  models.IntegerField()
	cantidad=  models.IntegerField()
	local= models.ManyToManyField(Local,null=True, blank=True)
	
	