from rest_framework import serializers
from tractorsApp.models import Tractor, Driver, TractorRent
from tractorsApp.validators import *
from django.http import JsonResponse

"""Modelo de serialização de como os objetos serão retornados"""

class TractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tractor
        #fields = ['id', 'owner', 'tractorYear', 'manufacter', 'lastReview', 'lastLocation', 'lastFuelDate']
        fields = '__all__'
    def validate(self, data):
        if not validateOwner(data['owner']):
            raise serializers.ValidationError({"owner": "Owner must have only letters", "FL_STATUS": False})
        if not validateTractorYear(data['tractorYear']):
            raise serializers.ValidationError({"tractorYear": "Invalid year! Use the format YYYY, greater than 1979", "FL_STATUS": False})
        return data


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
    
    def validate(self, data):
        if not validateName(data['name']):
            raise serializers.ValidationError({"name":"Name must have only letters", "FL_STATUS": False})
        if not validateCPF(data['cpf']):
            raise serializers.ValidationError({"cpf":"This CPF is not valid! Must have 11 digits without spaces and dots", "FL_STATUS": False})
        if not validateCNH(data['cnh']):
            raise serializers.ValidationError({"cnh":"This CNH is not valid! Must have 9 digits, without spaces and dots", "FL_STATUS": False})
        return data


class TractorRentSerializer(serializers.ModelSerializer):
    tractor = serializers.ReadOnlyField(source = 'tractor.identification')
    driver = serializers.ReadOnlyField(source = 'driver.name')
    class Meta:
        model = TractorRent
        exclude = ['id']  #trás todos


class ListDriverRentsSerializer(serializers.ModelSerializer):
    tractor = serializers.ReadOnlyField(source = 'tractor.identification')
    class Meta:
        model = TractorRent
        fields = ['tractor', 'date']


class ListTractorRentsSerializer(serializers.ModelSerializer):
    driver = serializers.ReadOnlyField(source = 'driver.name')
    class Meta:
        model = TractorRent
        fields = ['driver', 'date']