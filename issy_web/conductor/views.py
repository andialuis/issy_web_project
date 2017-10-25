from django.shortcuts import render

#necesario para restricciones en logeo
from django.contrib.auth.decorators import login_required

#necesario para trabajar con plantillas(CRUD)
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

from . import forms
from conductor.models import Auto
# Create your views here.


class AlquilarAuto(TemplateView):
	template_name= 'conductor/alquilar_auto.html'

def alquilar_auto_lista(request):
	'''
	form=forms.NewTopicForm()
	if request.method=='POST':
		form = forms.NewTopicForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("HOrror en form_name_view")
	return render(request,'first_app/form_page.html',{'form':form})
	'''
	print (request.POST)
	print (request.method)

	Webpage_list = Auto.objects.order_by('precio')
	date_dict ={'access_records':Webpage_list,'query_ok':"True"}
	#my_dict={'insert_me':"Hello I am from views.py",'query_ok':True}

	print (Webpage_list)
	return render(request,'conductor/alquilar_auto.html',context=date_dict)