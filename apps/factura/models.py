from django.db import models
from apps.producto.models import Producto
from apps.cliente.models import Cliente
# Create your models here.
class Pago(models.Model):
	tipo= models.CharField(max_length=60)

class Factura(models.Model):
	fecha= models.DateField()
	pago= models.ForeignKey(Pago, null=True, blank=True, on_delete=models.CASCADE)
	cliente= models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	producto= models.ManyToManyField(Producto)