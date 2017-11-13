from django import forms
from django.core import validators

from conductor.models import  Conductor



class ConductorForm(forms.ModelForm):
	class Meta():
		model = Conductor
		exclude = ('user',)
		fields ="__all__"

