from django.contrib import admin
from django.urls import path

from fire.views import HomePageView,ChartView,PieCountbySeverity,LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity,FireStationList, FireStationCreateView,FireStationUpdateView,FireStationDeleteView,FireFighterList,FireFighterCreateView,FireFighterUpdateView,FireFighterDeleteView, FireTruckList,FireTruckCreateView, FireTruckUpdateView,FireTruckDeleteView
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.map_incident, name='map-incident'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('fireStation_list', FireStationList.as_view(), name='fireStation-list'),
    path('fireStation_list/add', FireStationCreateView.as_view(), name='fireStation-add'),
    path('fireStation_list/<pk>', FireStationUpdateView.as_view(), name='fireStation-update'),
    path('fireStation_list/<pk>/delete', FireStationDeleteView.as_view(), name='fireStation-delete'),
    path('fireFighter_list', FireFighterList.as_view(), name='fireFighter-list'),
    path('fireFighter_list/add', FireFighterCreateView.as_view(), name='fireFighter-add'),
    path('fireFighter_list/<pk>', FireFighterUpdateView.as_view(), name='fireFighter-update'),
    path('fireFighter_list/<pk>/delete', FireFighterDeleteView.as_view(), name='fireFighter-delete'),
    path('fireTruck_list', FireTruckList.as_view(), name='fireTruck-list'),
    path('fireTruck_list/add', FireTruckCreateView.as_view(), name='fireTruck-add'),
    path('fireTruck_list/<pk>', FireTruckUpdateView.as_view(), name='fireTruck-update'),
    path('fireTruck_list/<pk>/delete', FireTruckDeleteView.as_view(), name='fireTruck-delete'),
]
