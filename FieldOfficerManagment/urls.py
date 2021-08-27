from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'FieldOfficerManagment'

urlpatterns = [
    url(r'^$', views.fieldOfficerDispachedList, name='index'),
    url(r'^create_Dispatch/$', views.create_Dispatch, name='create_Dispatch'),
    url(r'^getPoliceOfficer/(?P<policeStationName>[a-zA-Z ]+)/$', views.getPoliceOfficer, name='getPoliceOfficer'),
    url(r'^getpoliceStallName/(?P<policeStationName>[a-zA-Z ]+)/$', views.getpoliceStallName, name='getpoliceStallName'),
    url(r'^getOfficersByPoliceStall/(?P<stallName>[a-zA-Z ]+)/(?P<dispachedDate>\d{4}-\d{2}-\d{2})/$', views.getOfficersByPoliceStall, name='getOfficersByPoliceStall'),
]