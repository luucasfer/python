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
 
