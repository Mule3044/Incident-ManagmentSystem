from django.contrib.auth.models import Permission, User
from django.db import models


from datetime import datetime


class FieldOfficer(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    phoneNumber = models.CharField(max_length=20)
    policeStation = models.CharField(max_length=250)
    status = models.CharField(max_length=20)


    def __str__(self):
        return self.firstName + '-' + self.lastName


class FieldOfficerDispatch(models.Model):
    fieldOfficer = models.ForeignKey(FieldOfficer, on_delete=models.CASCADE)
    dispatchedDate = models.DateField()
    policeStallName = models.CharField(max_length=250)

    def __str__(self):
        return self.policeStallName
