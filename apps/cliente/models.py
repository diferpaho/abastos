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