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
		exclude = ('user',)
		fields ="__all__"

