from django.db import models
from issy_web.constants import ESTADO_CIVIL
import datetime
from django.core.urlresolvers import reverse
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()


class Conductor(models.Model):
	#user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,default='')
	user = models.OneToOneField("auth.User")
	nombre = models.CharField(max_length=264,blank=False,null=False)
	apellido = models.CharField(max_length=264,blank=False,null=False)
	estrellas = models.IntegerField(default=0,blank=False,null=False)
	estado = models.CharField(max_length=20)
	edad = models.IntegerField(blank=False,null=False)
	estado_civil = models.CharField(max_length = 1, choices = ESTADO_CIVIL, blank = False,
	null = False, default = ESTADO_CIVIL[0][0])
	ciudad = models.CharField(max_length=50,blank=False,null=False)
	inicio_app = models.DateField(default=datetime.date.today,blank=False,null=False)
	total_viajes = models.IntegerField(default=0,blank=False,null=False)
	tipo_licencia = models.CharField(max_length=8,blank=False,null=False)
	vencimiento_licencia = models.DateField(blank=False,null=False)
	telefono = models.IntegerField(blank=False,null=False)
	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse("conductor:conductor_info")


