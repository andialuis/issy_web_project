from django import forms
from django.core import validators

from conductor.models import  Conductor
from auto.models import Reviews



class ConductorForm(forms.ModelForm):
	class Meta():
		model = Conductor
		exclude = ('user',)
		fields ="__all__"


class ReviewForm(forms.ModelForm):
	class Meta():
		model = Reviews
		fields ="__all__"
		exclude = ('contrato',)
		

'''	def get_form_kwargs(self, **kwargs):
		form_kwargs = super(TestCreateView, self).get_form_kwargs(**kwargs)
		form_kwargs["pk"] = self.request.user
		return form_kwargs
'''
