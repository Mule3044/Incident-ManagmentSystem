from django.contrib import admin
from IncidentManagment.models import IncidentType, Incident

# Register your models here.

admin.site.register(IncidentType)
admin.site.register(Incident)
