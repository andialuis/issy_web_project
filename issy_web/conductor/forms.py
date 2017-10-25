from django import forms
from django.core import validators

from conductor.models import Auto  

class NewAuto(forms.ModelForm):
	class Meta():
		model= Auto
		fields ="__all__"
