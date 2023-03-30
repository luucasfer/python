from django.shortcuts import render
from rest_framework import viewsets
from quickstart.models import *
from quickstart.serializers import *


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TuctorSerializer 
 
