from django.contrib import admin

# Register your models here.
from conductor.models import Conductor
from auto.models import Reviews


# Register your models here.


admin.site.register(Conductor)
admin.site.register(Reviews)

