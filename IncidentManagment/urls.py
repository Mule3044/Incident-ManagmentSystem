from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'IncidentManagment'

urlpatterns = [
    url(r'^incidentList/$', views.incidentList, name='incidentList'),
    url(r'^create_Incident/$', views.create_Incident, name='create_Incident'),
    url(r'^AssignPoliceForIncident/$', views.AssignPoliceForIncident, name='AssignPoliceForIncident'),
    url(r'^AssignPoliceStallForIncident/$', views.AssignPoliceStallForIncident, name='AssignPoliceStallForIncident'),
]