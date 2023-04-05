from rest_framework import serializers, status
from rest_framework.response import Response
from quickstart.models import Tutor, Abrigo, Pet
from adopet.validators import *
from django.http import JsonResponse
from adopet.validators import validateEmail, validateName


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['id', 'name', 'email', 'phone', 'city', 'about']
        
    def validate(self, data):
        if not validateEmail(data['email']):
            raise serializers.ValidationError("Este email não é válido", status=status.HTTP_400_BAD_REQUEST)
        if not validateName(data['name']):
            raise serializers.ValidationError("O nome deve conter apenas letras", status=status.HTTP_400_BAD_REQUEST)
        return data
    

            
class AbrigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abrigo
        fields = ['id', 'name', 'phone', 'city', 'state']
        
    def validate(self, data):
        if not validateName(data['name']):
            raise serializers.ValidationError("O nome deve conter apenas letras", status=status.HTTP_400_BAD_REQUEST)
        return data



class PetSerializer(serializers.ModelSerializer):
    #address     =  serializers.ReadOnlyField(source =  'abrigo.city')
    class Meta:
        model = Pet
        fields = '__all__'
        
    def validate(self, data):
        if not validateName(data['name']):
            raise serializers.ValidationError("O nome deve conter apenas letras", status=status.HTTP_400_BAD_REQUEST)
        return data