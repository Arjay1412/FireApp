from django.forms import ModelForm
from django import forms
from .models import Incident, Locations, Firefighters, FireStation, FireTruck, WeatherConditions

class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"

class FireFighterForm(ModelForm):
    class Meta:
        model = Firefighters
        fields = "__all__"

class FireTruckForm(ModelForm):
    class Meta:
        model = FireTruck
        fields = "__all__"