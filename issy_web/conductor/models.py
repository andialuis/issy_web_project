from django.db import models
from issy_web.constants import ESTADO_CIVIL
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.

class Auto(models.Model):
	modelo= models.CharField(max_length=264)
	plazas= models.CharField(max_length=264)
	aire_acondicionado= models.CharField(max_length=264)
	tipo_transmision= models.CharField(max_length=264)
	lugar_recodiga= models.CharField(max_length=264)
	precio= models.FloatField()
	jornada= models.IntegerField()
	is_alquiled= models.BooleanField()
	#def __str__(self):
	#	return self.modelo

class Conductor(models.Model):
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
	correo = models.CharField(max_length=50,blank=False,null=False)
	telefono = models.IntegerField(blank=False,null=False)
	def __str__(self):
		return (self.nombre+" "+self.apellido)

class Resenha(models.Model):
    emisor = models.CharField(max_length=264,blank=False,null=False)
    receptor = models.ForeignKey(Conductor,blank=False,null=False,on_delete=models.CASCADE,)
    estrellas = models.IntegerField(blank=False,null=False,
                                    validators=[MaxValueValidator(5),MinValueValidator(1)])
    comentario = models.TextField(blank=False,null=False)
    fecha = models.DateField(default=datetime.date.today,blank=False,null=False)