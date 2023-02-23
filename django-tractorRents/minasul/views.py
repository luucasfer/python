from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from minasul.models import Tractor, Driver, TractorRent
from minasul.serializer import TractorSerializer, DriverSerializer, TractorRentSerializer, ListDriverRentsSerializer, ListTractorRentsSerializer


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
