from django.db import models

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
	def __str__(self):
		return self.modelo

class Conductor(models.Model):
	nombre = models.CharField(max_length=264)
	apellido = models.CharField(max_length=264)
	estrellas = models.IntegerField()
	estado = models.CharField(max_length=20)
	edad = models.IntegerField()
	estado_civil = models.IntegerField()
	ciudad = models.CharField(max_length=50)
	inicio_app = models.DateField()
	total_viajes = models.IntegerField()
	tipo_licencia = models.CharField(max_length=8)
	vencimiento_licencia = models.DateField()
	correo = models.CharField(max_length=50)
	telefono = models.IntegerField()
	def __str__(self):
		return self.name