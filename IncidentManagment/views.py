from django.http import JsonResponse

from django.shortcuts import render
from geoserver.catalog import Catalog
import pg8000
from IncidentManagment.forms import IncidentForm
from IncidentManagment.models import Incident, IncidentType


def create_Incident(request):

    conn = pg8000.connect(database="IncidentManagmentDb", user="postgres",password="postgres")
    cursor = conn.cursor()
    cursor.execute("Select woreda,gid from nfs_woredas")
    results = cursor.fetchall()
    woreda_List=[]

    for row in results:
        woreda, gid=row
        slDict={}
        slDict['woreda'] = woreda
        slDict['gid'] = gid

        woreda_List.append(slDict)

    print(woreda_List)
    cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")
    lay1 = cat.get_layer("nfs_boundary")

    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.save()
    else:
         form = IncidentForm()

    incidentTypeList = IncidentType.objects.all().values('id', 'name')



    context = {
            "form": form,
            "lay1": lay1,
            "incidentTypeList":incidentTypeList,
            "woreda_List":woreda_List
        }
    return render(request, 'IncidentManagment/Create_Incident.html', context)



def incidentList(request):
    cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")
    lay1 = cat.get_layer("nfs_boundary")

    incidents = Incident.objects.all()
    incidentTypeList = IncidentType.objects.all()

    incident_List=[]

    for row in incidents:

        for rowIncidentType in incidentTypeList:

            if row.incidentType.id == rowIncidentType.id:
                incidentDict={}
                incidentDict['incidentId'] = row.id
                incidentDict['idIncidentType'] = rowIncidentType.id
                incidentDict['name'] = rowIncidentType.name
                incidentDict['placeName'] = row.placeName
                incidentDict['woreda'] = row.woreda
                incidentDict['callerName'] = row.callerName
                incidentDict['phoneNumber'] = row.phoneNumber
                incidentDict['description'] = row.description
                incidentDict['incidentDate'] = row.incidentDate
                incidentDict['longitude'] = row.longitude
                incidentDict['latitude'] = row.latitude
                incidentDict['status'] = row.status
                incidentDict['remark'] = rowIncidentType.remark
                incident_List.append(incidentDict)
                break
    print (incident_List)

    context = {
        "lay1": lay1,
        "incidents":incident_List
    }
    return render(request, 'IncidentManagment/Incident_List.html', context)

def AssignPoliceForIncident(request):

    cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")
    lay1 = cat.get_layer("nfs_boundary")



    context = {
        "lay1": lay1
    }
    return render(request, 'IncidentManagment/AssignStall_Incident.html', context)


def AssignPoliceStallForIncident(request):

    cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")
    lay1 = cat.get_layer("nfs_boundary")



    context = {
        "lay1": lay1
    }
    return render(request, 'IncidentManagment/AssignPoliceStallForIncident.html', context)