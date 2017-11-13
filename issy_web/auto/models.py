from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

User = get_user_model()



# Create your models here.

class Auto(models.Model):
	user = models.ForeignKey("auth.User",null=True)
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

	def get_absolute_url(self):
		return reverse("auto:auto_list")

	