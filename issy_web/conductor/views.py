from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
#necesario para restricciones en logeo
from django.contrib.auth.decorators import login_required

#necesario para trabajar con plantillas(CRUD)
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from braces.views import SelectRelatedMixin
from django.views import generic
from .forms import ConductorForm
from conductor.models import Conductor
from auto.models import Reviews
from auto.models import Auto
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


class HistoConductor(TemplateView):
	template_name= 'conductor/historial_conductor.html'

def info_auto_detalle(request,pk):

	Webpage_list = Auto.objects.get(pk=pk)
	return render(request,'conductor/info_auto.html',{'info_auto_detalle':Webpage_list})



 

def ConductorInfo(request):
	try:
		conductor = Conductor.objects.get(user=request.user)
		reviews = Reviews.objects.filter(contrato__User_contrata=request.user)
		print (reviews)
	except Conductor.DoesNotExist:
		conductor =None
	return render(request,'conductor/conductor_info.html',{'conductor':conductor,'reviews':reviews})




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

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user_sender = self.request.user
		self.object.save()
		return super().form_valid(form)

class ConductorUpdate(LoginRequiredMixin,UpdateView):

	form_class = ConductorForm
	model = Conductor
	redirect_field_name = "conductor/conductor_info.html"




@login_required
def alquilar_auto_lista(request):

	Webpage_list = Auto.objects.exclude(user=request.user).filter(is_alquiled=False).order_by('precio')
	date_dict ={'access_records':Webpage_list,'query_ok':"True"}

	print (Webpage_list)
	return render(request,'conductor/alquilar_auto.html',context=date_dict)