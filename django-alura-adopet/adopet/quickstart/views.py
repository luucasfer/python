from django.shortcuts import render
from rest_framework import viewsets
from quickstart.models import *
from quickstart.serializers import *


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer 
    
    def list(self, request):
        tutors = Tutor.objects.all()
        if tutors.count() == 0:
            return Response({"mensagem": "Não há nenhum tutor cadastrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TutorSerializer(tutors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"mensagem":"Tutor deletado com sucesso"}, status=status.HTTP_200_OK)
    def perform_destroy(self, instance):
        instance.delete()
 


class AbrigoViewSet(viewsets.ModelViewSet):
    queryset = Abrigo.objects.all()
    serializer_class = AbrigoSerializer 
    
    def list(self, request):
        abrigos = Abrigo.objects.all()
        if abrigos.count() == 0:
            return Response({"mensagem": "Não há nenhum Abrigo cadastrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AbrigoSerializer(abrigos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"mensagem":"Abrigo deletado com sucesso"}, status=status.HTTP_200_OK)
    def perform_destroy(self, instance):
        instance.delete()



class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer 
    
    def list(self, request):
        pets = Pet.objects.all()
        if pets.count() == 0:
            return Response({"mensagem": "Não há nenhum Pet cadastrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"mensagem":"Pet deletado com sucesso"}, status=status.HTTP_200_OK)
    def perform_destroy(self, instance):
        instance.delete()