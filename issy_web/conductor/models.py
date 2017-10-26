from django.db import models

# Create your models here.

class Auto(models.Model):
	modelo= models.CharField(max_length=264)
	plazas= models.CharField(max_length=264)
	aire_acondicionado= models.CharField(max_length=264)
	tipo_transmision= models.CharField(max_length=264)
	lugar_recodiga= models.CharField(max_length=264)
	precio= models.FloatField()
	jornada= models.IntegerField(max_length=264)
	is_alquiled= models.BooleanField()
	#def __str__(self):
	#	return self.modelo



