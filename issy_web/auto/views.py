from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

from auto.forms import AutoForm

from django.urls import  reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Auto,Contrato
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.db.models import Q
User = get_user_model()
# Create your views here.


class AutoListView(ListView):
	model = Auto

	def get_queryset(self):
		return Auto.objects.filter(user=self.request.user).order_by('-precio')



class AutoDetailView(DetailView):
	model = Auto

class CreateAutoView(LoginRequiredMixin,CreateView):

	login_url ="/login/"
	redirect_field_name = "auto/auto_detail.html"
	form_class= AutoForm
	model = Auto
	def form_valid(self, form):
		self.object = form.save(commit=False)
		print (self.request.user.username)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)


class AutoUpdateView(LoginRequiredMixin,UpdateView):

	login_url ="/login/"
	redirect_field_name = "auto/auto_detail.html"
	form_class= AutoForm
	model = Auto


class AutoDeleteView(LoginRequiredMixin,DeleteView):
	model = Auto
	success_url = reverse_lazy("auto:auto_list")



class AutoContratos(LoginRequiredMixin,ListView):
	model= Contrato
	template_name = 'auto/contrato_list.html'
	def get_context_data(self):
		mContrato= Contrato.objects.filter(Q(User_contrata=self.request.user)| Q(User_alquila=self.request.user))
		dict_res={'contrato_list':mContrato,'is_for_me':False}
		return dict_res

@require_http_methods(["GET"])
def GetContratosForMe(request):
	mContrato= Contrato.objects.filter(User_alquila=request.user)
	dict_res={'contrato_list':mContrato,'is_for_me':True}
	return render(request,'auto/contrato_list.html',dict_res)

@require_http_methods(["GET"])
def GetContratosToOther(request):
	mContrato= Contrato.objects.filter(User_contrata=request.user)
	dict_res={'contrato_list':mContrato,'is_for_me':False}
	return render(request,'auto/contrato_list.html',dict_res)

@require_http_methods(["GET"])
def AcceptContract(request,pk):
	Contrato.objects.filter(pk=pk).update(hired_status='2')
	mContrato= Contrato.objects.filter(User_contrata=request.user)
	dict_res={'contrato_list':mContrato,'is_for_me':False}
	return render(request,'auto/contrato_list.html',dict_res)

@require_http_methods(["GET"])
def FinishContract(request,pk):
	Contrato.objects.filter(pk=pk).update(hired_status='3')
	mContrato= Contrato.objects.filter(User_contrata=request.user)
	dict_res={'contrato_list':mContrato,'is_for_me':False}
	return render(request,'auto/contrato_list.html',dict_res)









@login_required
def AutoOfertar(request,pk):
	p= Auto.objects.filter(pk=pk).update(is_alquiled=True)
	print(p)
	ofertas=Auto.objects.filter(is_alquiled=True,pk=pk)

	return render(request,'auto/auto_list.html',{'ofertas':ofertas})


@login_required
def AutoOfertados(request):

	ofertas=Auto.objects.filter(is_alquiled=True,user=request.user)

	return render(request,'auto/auto_list.html',{'auto_list':ofertas})


@login_required
def AutoSinOfertar(request):

	ofertas=Auto.objects.filter(is_alquiled=False,user=request.user)

	return render(request,'auto/auto_list.html',{'auto_list':ofertas})


@login_required
@require_http_methods(["GET"])
def AutoContratar(request,owner,auto):

	print (owner)
	print (auto)
	owner = User.objects.get(username=owner)
	print (owner)
	Auto_status=Auto.objects.get(is_alquiled=False,user=owner,pk=auto)
	if Auto_status == None:
		return HttpResponse('auto already hired')
	Auto.objects.filter(user=owner,pk=auto).update(is_alquiled=True)
	contract = Contrato(User_alquila=owner,User_contrata=request.user,auto=Auto_status)
	try:
		contract.save()
		return HttpResponse(contract)
	except IntegrityError as e:
		return HttpResponse('error reference key')


	