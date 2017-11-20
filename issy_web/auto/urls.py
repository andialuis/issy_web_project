from django.conf.urls import url

from . import views

app_name='auto'


urlpatterns = [

url(r'^$',views.AutoListView.as_view(),name="auto_list"),
url(r'^(?P<pk>\d+)$',views.AutoDetailView.as_view(),name='auto_detail'),
url(r'^new/$',views.CreateAutoView.as_view(),name="auto_crear"),
url(r'^(?P<pk>\d+)/edit/$',views.AutoUpdateView.as_view(),name="auto_edit"),
url(r'^(?P<pk>\d+)/remove/$',views.AutoDeleteView.as_view(),name="auto_remove"),
url(r'^(?P<pk>\d+)/ofertar/$',views.AutoOfertar,name="auto_ofertar"),
url(r'^ofertados/$',views.AutoOfertados,name="auto_ofertados"),
url(r'^sinofertar/$',views.AutoSinOfertar,name="auto_sin_ofertar"),
url(r'^contratos/$',views.AutoContratos.as_view(),name="contratos"),
url(r'^contratar/(?P<owner>\w+)/(?P<auto>\w+)$',views.AutoContratar,name="contratar"),
url(r'^ofertas_hacia_mi/$',views.GetContratosForMe,name="ofertas_hacia_mi"),
url(r'^ofertas_hacia_otros/$',views.GetContratosToOther,name="ofertas_hacia_otros"),
url(r'^aceptar_contrato/(?P<pk>\d+)/$',views.AcceptContract,name="aceptar_contrato"),
url(r'^finalizar_contrato/(?P<pk>\d+)/$',views.FinishContract,name="finalizar_contrato"),


]
