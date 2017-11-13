from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

from auto.forms import AutoForm

from django.urls import  reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Auto
# Create your views here.


class AutoListView(ListView):
	model = Auto

	#def get_queryset(self):
	#	return auto.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')



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






