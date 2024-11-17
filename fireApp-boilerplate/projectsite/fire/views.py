from django.shortcuts import render
from django.views.generic.list import ListView
from fire.models import Locations, Incident, FireStation
from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth

from django.db.models import Count
from datetime import datetime

class HomePageView(ListView):
    model = Locations
    context_object_name = 'home'
    template_name = "home.html"

class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass

def PieCountbySeverity(request): 
    query = ''' 
    SELECT severity_level, COUNT(*) as count 
    FROM fire_incident
    GROUP BY severity_level
    ''' 
    data = {}
    with connection.cursor() as cursor: 
        cursor.execute(query)
        rows = cursor.fetchall()
    
    if rows: 
        # Construct the dictionary with severity level as keys and count as values 
        data = {severity: count for severity, count in rows}
    else:
        data = {}
    return JsonResponse(data)

def map_station(request):
    # Retrieve fire station data from the database
    fireStations = FireStation.objects.values('name', 'latitude', 'longitude')

    # Convert latitude and longitude to float for proper handling in JavaScript
    for fs in fireStations:
        fs['latitude'] = float(fs['latitude'])
        fs['longitude'] = float(fs['longitude'])

    # Convert QuerySet to a list
    fireStations_list = list(fireStations)

    # Prepare context to pass to the template
    context = {
        'fireStations': fireStations_list,
    }

    # Render the template with the fire station data
    return render(request, 'map_station.html', context)
