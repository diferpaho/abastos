from django import forms

from apps.producto.models import Local, Producto 

class LocalForm(forms.ModelForm):
	

	class Meta:
		model= Local
		fields=[
		'nombre',
		'ubicacion',
		'administrador',
		
		]
		labels={
		'nombre': 'Nombre',
		'ubicacion': 'Ubicacion',
		'administrador': 'Administrador',
		
		
		}
		widgets={
		'nombre':forms.TextInput(attrs={'class':'form-control'}),
		'ubicacion':forms.TextInput(attrs={'class':'form-control'}),
		'administrador':forms.TextInput(attrs={'class':'form-control'}),
		
		}

class ProductoForm(forms.ModelForm):
	
	class Meta:
		model=Producto
		fields=[
		'nombre',
		'descripcion',
		'precio',
		'cantidad',
		]
				
		labels={
		'nombre': 'Nombre',
		'descripcion': 'Descripcion',
		'precio': 'Precio',
		'cantidad': 'Cantidad',
		}
		widgets={
		'nombre':forms.TextInput(attrs={'class':'form-control'}),
		'descripcion':forms.TextInput(attrs={'class':'form-control'}),
		'precio':forms.TextInput(attrs={'class':'form-control'}),
		'cantidad':forms.TextInput(attrs={'class':'form-control'}),
		}
