from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
#necesario para restricciones en logeo
from django.contrib.auth.decorators import login_required

#necesario para trabajar con plantillas(CRUD)
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

from .forms import ConductorForm
from conductor.models import Auto,Conductor

# Create your views here.

class AlquilarAuto(TemplateView):
	template_name= 'conductor/alquilar_auto.html'

class HomeConductor(TemplateView):
	template_name= 'conductor/home_conductor.html'

class InfoAuto(TemplateView):
	template_name= 'conductor/info_auto.html'


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

def info_auto(request,pk):
	auto = get_object_or_404(Auto,pk=pk)
	Webpage_list = Auto.objects.get(pk=pk)


	#print(Webpage_list.precio)
	#form = CommentForm()
	return render(request,'conductor/alquilar_auto.html',{'info_auto':Webpage_list})

class ConductorInfo(TemplateView):
	template_name = 'conductor/conductor_info.html'

class ConductorCreate(CreateView):
	model = Conductor
	form_class = ConductorForm
	template_name = 'registration/registro_conductor.html'
	success_url = reverse_lazy('home_conductor')
