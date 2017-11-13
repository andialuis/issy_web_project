from django.conf.urls import url

from . import views

app_name='auto'


urlpatterns = [

    url(r'^$',views.AutoListView.as_view(),name="auto_list"),
    url(r'^(?P<pk>\d+)$',views.AutoDetailView.as_view(),name='auto_detail'),
    url(r'^new/$',views.CreateAutoView.as_view(),name="auto_crear"),
    url(r'^(?P<pk>\d+)/edit/$',views.AutoUpdateView.as_view(),name="auto_edit"),
    url(r'^(?P<pk>\d+)/remove/$',views.AutoDeleteView.as_view(),name="auto_remove"),
]
