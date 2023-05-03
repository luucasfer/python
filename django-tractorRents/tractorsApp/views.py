import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from influxdb.exceptions import InfluxDBClientError
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from setup import settings
from tractorsApp.models import Driver, Tractor, TractorRent
from tractorsApp.serializer import (DriverSerializer,
                                    ListDriverRentsSerializer,
                                    ListTractorRentsSerializer,
                                    TractorRentSerializer, TractorSerializer)
from tractorsApp.utils import influxConnection

"""Classes para chamar os modelos de serialização e fazer o return
Permitem definir as interações da sua API (GET,POST,PUT,DELETE...) 
e permitir que a estrutura  REST construa os URLs dinamicamente com um objeto roteador."""

class TractorsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tratores"""
    queryset = Tractor.objects.all()
    serializer_class = TractorSerializer #quem é classe responsavel por serializar?
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

class DriversViewSet(viewsets.ModelViewSet):
    """Exibindo todos pilotos"""
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class TractorRentViewSet(viewsets.ModelViewSet):
    """Exibindo todos aluguéis"""
    queryset = TractorRent.objects.all()
    serializer_class = TractorRentSerializer

class ListDriverRentsViewSet(generics.ListAPIView):  
    """Exibindo todos alugueis de um piloto especifico"""
    def get_queryset(self):
        query_set = TractorRent.objects.filter(driver_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListDriverRentsSerializer

class ListTractorRentsViewSet(generics.ListAPIView):  
    """Exibindo todos pilotos que alugaram um trator especifico"""
    def get_queryset(self):
        query_set = TractorRent.objects.filter(tractor_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListTractorRentsSerializer

class InfluxLocationViewSet(View):
    def post(self, telemetry): 
        try:
            telemetry = json.loads(telemetry.body)
            influxConnection().switch_database(settings.INFLUXDB_DATABASE)
            for eachLocation in telemetry["lastLocations"]:
                json_body = [
                    {
                        "measurement": telemetry["tractorIdentification"],
                        "tags": {
                            "tractorIdentification": telemetry["tractorIdentification"],                
                        },
                        "time": eachLocation["time"],
                        "fields":{
                            "latlong":eachLocation["latlong"]
                        }
                    }
                ]
                influxConnection().write_points(json_body)
            return JsonResponse({"message": "Location inserted at InfluxDB", "FL_STATUS": True}, status=200)
        except InfluxDBClientError as e:
            return JsonResponse({"message": f'Influx Insert Error: {str(e)}', "FL_STATUS":False}, status=500)


    def get(self, request, tractorIdentification):
        try:
            influxConnection().switch_database(settings.INFLUXDB_DATABASE)
            results = list(influxConnection().query(f'SELECT * FROM "{tractorIdentification}" WHERE time >= now() - 24h AND time <= now()').get_points())
            return JsonResponse({"message": results,  "FL_STATUS":True}, status=200)
        except InfluxDBClientError as e:
            return JsonResponse({"message": f'Influx Search error {tractorIdentification}: {str(e)}', "FL_STATUS":False}, status=500)
        
