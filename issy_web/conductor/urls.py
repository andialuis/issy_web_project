
from django.conf.urls import url
from conductor import views

app_name = 'conductor'
urlpatterns = [
url(r'^$',views.AlquilarAuto.as_view(),name="alquilar_auto"),
url(r'^buscar_autos/$',views.alquilar_auto_lista,name="buscar_autos"),
url(r'^home_conductor/$',views.HomeConductor.as_view(),name="home_conductor"),
url(r'^duenho/home_duenho$',views.HomeDuenho.as_view(),name="home_duenho"),
url(r'^conductor/registro_conductor$',views.ConductorCreate.as_view(),name = "registro_conductor"),
url(r'^conductor_info/$',views.ConductorInfo,name="conductor_info"),
url(r'^perfil/(?P<pk>\d+)/edit/$',views.ConductorUpdate.as_view(),name="perfil_edit"),
url(r'^perfil/new/$',views.ConductorProfileCreate.as_view(),name="perfil_crear"),
url(r'^info_auto',views.InfoAuto.as_view(),name="info_auto"),
url(r'^$',views.Index.as_view(),name="index"),
url(r'^auto/(?P<pk>\d+)/detalle/$',views.info_auto,name="info_auto2"),
url(r'^conductor/historial_conductor$',views.HistoConductor.as_view(),name="historial_conductor"),

]