# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse

from django.shortcuts import HttpResponse, get_object_or_404

from django.shortcuts import render
from geoserver.catalog import Catalog
import pg8000, json
# Create your views here.
from FieldOfficerManagment.forms import FieldOfficerDispatchForm, FieldOfficerForm
from FieldOfficerManagment.models import FieldOfficer, FieldOfficerDispatch
from django.core.serializers.json import DjangoJSONEncoder


def fieldOfficerDispachedList(request):
    cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")
    lay1 = cat.get_layer("nfs_boundary")



    context = {
        "lay1": lay1
    }
    return render(request, 'FieldOfficerManagment/fieldOfficerDispachedList.html', context)

def create_Dispatch(request):

        conn = pg8000.connect(database="IncidentManagmentDb", user="postgres",password="postgres")
        cursor = conn.cursor()
        cursor.execute("Select name,gid from nfs_policestations")
        results = cursor.fetchall()
        policeStationList=[]

        for row in results:
            pname, gid=row
            slDict={}
            slDict['policeStation'] = pname
            slDict['gid'] = gid

            policeStationList.append(slDict)


        cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")
        lay1 = cat.get_layer("nfs_boundary")


        form = FieldOfficerDispatchForm(request.POST or None, request.FILES or None)
        if form.is_valid():
                dispatch = form.save(commit=False)
                dispatch.save()

                field_officer_id=form.cleaned_data["fieldOfficer"].id
                field_officer=FieldOfficer.objects.get(id=field_officer_id)
                field_officer.status = "OnDuty"
                field_officer.save()




        context = {
            "form": form,
            "lay1": lay1,
            "policeStationList":policeStationList


        }
        return render(request, 'FieldOfficerManagment/CreateFieldOfficerDispach.html', context)


##views.py
def getPoliceOfficer(request,policeStationName):
    offcerList= FieldOfficer.objects.filter(policeStation=policeStationName, status='Ready').values('id', 'firstName','lastName')
    data =json.dumps(list(offcerList))
    return JsonResponse(data,safe=False)

##views.py
def getpoliceStallName(request,policeStationName):
    conn = pg8000.connect(database="IncidentManagmentDb", user="postgres",password="postgres")
    cursor = conn.cursor()
    cursor.execute("Select stallname from nfs_policestalls where stationnam='" + policeStationName + "'")
    stallList = cursor.fetchall()
    data =json.dumps(list(stallList))

    return JsonResponse(data,safe=False)


##views.py
def getOfficersByPoliceStall(request,stallName, dispachedDate):
    offcerList= FieldOfficer.objects.filter(fieldofficerdispatch__policeStallName=stallName,fieldofficerdispatch__dispatchedDate=dispachedDate).values('id', 'firstName','lastName','phoneNumber')
    data =json.dumps(list(offcerList))
    print(data)
    return JsonResponse(data,safe=False)
