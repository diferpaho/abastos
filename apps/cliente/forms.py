from django import forms

from apps.cliente.models import Cliente, Registrar

class ClienteForm(forms.ModelForm):
	fecha= forms.DateField(widget=forms.DateInput)

	class Meta:
		model= Cliente
		fields=[
		'nombre',
		'apellido',
		'fecha',
		'email',
		'telefono',
		'direccion',
		
		]
		labels={
		'nombre': 'Nombre',
		'apellido': 'Apellidos',
		'fecha': 'Fecha',
		'email': 'Correo',
		'telefono': 'Telefono',
		'direccion': 'Direccion',
		
		}
		widgets={
		'nombre':forms.TextInput(attrs={'class':'form-control'}),
		'apellido':forms.TextInput(attrs={'class':'form-control'}),
		'fecha':forms.DateInput(attrs={'class':'form-control'}),
		'email':forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'direccion':forms.TextInput(attrs={'class':'form-control'}),
		
		}

class RegistrarForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model=Registrar
		fields=[
		'nombreUsuario',
		'password',
		]
		labels={
		'nombreUsuario': 'Usuario',
		'password': 'Password',
		}
		widgets={
		'nombreUsuario':forms.TextInput(attrs={'class':'form-control'}),
		'password':forms.TextInput(attrs={'class':'form-control'}),
		}
