from django import forms
from django.core import validators

from conductor.models import Auto, Conductor

class NewAuto(forms.ModelForm):
	class Meta():
		model= Auto
		fields ="__all__"

class ConductorForm(forms.ModelForm):
	class Meta():
		model = Conductor
		fields = [
			'nombre',
		 	'apellido',
		 	'edad',
		 	'estado_civil',
		 	'ciudad',
		 	'tipo_licencia',
		 	'vencimiento_licencia',
		 	'correo',
		 	'telefono',
		 ]
		labels = {
			'nombre' :'Nombres',
			'apellido':'Apellidos',
			'edad':'Edad',
			'estado_civil':'Estado civil',
			'ciudad':'Ciudad',
			'tipo_licencia':'Tipo de Licencia',
			'vencimiento_licencia':'Vencimiento de la licencia',
			'correo':'Correo',
			'telefono':'Telefono',
		}

