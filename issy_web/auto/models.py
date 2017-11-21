from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

User = get_user_model()

HIRED_STATUS=(
    ('1', 'espera'),
    ('2', 'aceptado'),
    ('3', 'finalizado'),

)

# Create your models here.

class Auto(models.Model):
	user = models.ForeignKey("auth.User",null=True)
	modelo= models.CharField(max_length=264)
	plazas= models.CharField(max_length=264)
	aire_acondicionado= models.CharField(max_length=264)
	tipo_transmision= models.CharField(max_length=264)
	lugar_recogida= models.CharField(max_length=264)
	precio= models.FloatField()
	jornada= models.IntegerField()
	is_alquiled= models.BooleanField()
	def __str__(self):
		return self.modelo

	def get_absolute_url(self):
		return reverse("auto:auto_list")



class Contrato(models.Model):
	User_alquila=models.ForeignKey("auth.User",null=True,related_name="user_alquila")
	User_contrata=models.ForeignKey("auth.User",null=True,related_name="user_contrata")
	auto =models.ForeignKey(Auto,null=True,related_name="auto_contrata")
	hired_status=models.CharField(max_length = 1, choices = HIRED_STATUS,
	null = False, default = HIRED_STATUS[0][0])
	#class Meta:
	#	unique_together = (('User_alquila', 'User_contrata','auto'),)