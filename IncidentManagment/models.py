from django.contrib.auth.models import Permission, User
from django.db import models


from datetime import datetime


class IncidentType(models.Model):
    name = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)



    def __str__(self):
        return self.name


class Incident(models.Model):
    incidentType = models.ForeignKey(IncidentType, on_delete=models.CASCADE)
    placeName = models.CharField(max_length=250)
    woreda = models.CharField(max_length=250)
    callerName= models.CharField(max_length=250)
    phoneNumber= models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    incidentDate = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=250)


    def __str__(self):
        return self.placeName