
from django.conf.urls import url
from conductor import views


urlpatterns = [
url(r'^conductor/$',views.AlquilarAuto.as_view(),name="alquilar_auto"),
url(r'^conductor/lista_autos$',views.alquilar_auto_lista,name="lista_autos"),
url(r'^conductor/home_conductor$',views.HomeConductor.as_view(),name="home_conductor"),
url(r'^duenho/home_duenho$',views.HomeDuenho.as_view(),name="home_duenho"),
url(r'^conductor/conductor_info$',views.ConductorInfo.as_view(),name="conductor_info"),
url(r'^conductor/info_auto$',views.InfoAuto.as_view(),name="info_auto"),
url(r'^$',views.AlquilarAuto.as_view(),name="alquilar_auto"),

]