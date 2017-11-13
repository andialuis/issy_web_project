from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
#necesario para restricciones en logeo
from django.contrib.auth.decorators import login_required

#necesario para trabajar con plantillas(CRUD)
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from braces.views import SelectRelatedMixin
from django.views import generic
from .forms import ConductorForm
from conductor.models import Auto,Conductor
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class AlquilarAuto(TemplateView):
	template_name= 'conductor/alquilar_auto.html'

class HomeConductor(TemplateView):
	template_name= 'conductor/home_conductor.html'

class HomeDuenho(TemplateView):
	template_name= 'duenho/home_duenho.html'

class InfoAuto(TemplateView):
	template_name= 'conductor/info_auto.html'
class HistoConductor(TemplateView):
	template_name= 'conductor/historial_conductor.html'


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
	return render(request,'conductor/info_auto.html',{'info_auto':Webpage_list})

'''class ConductorInfo2(request,user):
	Webpage_list = Conductor.objects.order_by('precio')
	template_name = 'conductor/conductor_info.html'

class CreateProfileConductor(LoginRequiredMixin,CreateView):

	login_url ="/login/"
	redirect_field_name = "conductor/conductor_info.html"
	form_class= ConductorForm
	model = Conductor'''

def ConductorInfo(request):
	print(request.user.username)
	consulta = Conductor.objects.filter(user=request.user)

	print(len(consulta))
	#print(consulta.precio)
	#form = CommentForm()
	return render(request,'conductor/conductor_info.html',{'conductor':consulta})


#lanza plantilla   nombre_modelo_form
#class CreateProfileConductor(LoginRequiredMixin, generic.CreateView):
#    fields = ("name", "description")
#    model = Group


class ConductorCreate(CreateView):
	model = Conductor
	form_class = ConductorForm
	template_name = 'registration/registro_conductor.html'
	success_url = reverse_lazy('home_conductor')

class Index(TemplateView):
	template_name = 'index.html'



class ConductorProfileCreate(LoginRequiredMixin,CreateView):
	form_class = ConductorForm
	model = Conductor
	redirect_field_name = "conductor/conductor_info.html"




class ConductorUpdate(LoginRequiredMixin,UpdateView):

	form_class = ConductorForm
	model = Conductor
	redirect_field_name = "conductor/conductor_info.html"

	'''model = Conductor
	form_class = ConductorForm
	redirect_field_name = "conductor_form.html"
	success_url = reverse_lazy('conductor:home_conductor')
	login_url = '/login/'
	def get_success_url(self):
		userid = self.kwargs['pk']
		return reverse_lazy('conductor:home_conductor', kwargs={'pk': userid})
'''