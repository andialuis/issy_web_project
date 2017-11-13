from django import forms
from django.core import validators

from .models import Auto

class AutoForm(forms.ModelForm):
	class Meta():
		model = Auto
		exclude = ('user',)
		fields ="__all__"


class NewAuto(forms.ModelForm):
	class Meta():
		model= Auto
		fields ="__all__"