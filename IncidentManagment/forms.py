from django.contrib.auth.models import User
from django import forms
from .models import Incident, IncidentType


class IncidentTypeForm(forms.ModelForm):

    class Meta:
        model = IncidentType
        fields = ['name', 'remark']


class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ['incidentType', 'placeName','woreda',
                 'callerName','phoneNumber','description',
                 'incidentDate','latitude','longitude','status']