from rest_framework import serializers, status
from rest_framework.response import Response
from quickstart.models import Tutor
from adopet.validators import *
from django.http import JsonResponse
from adopet.validators import validateEmail, validateName

class TuctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['id', 'name', 'email', 'phone', 'city', 'about']
        #fields = '__all__'
    def validate(self, data):
        if not data:
            raise serializers.ValidationError("Não há nenhum tutor cadastrado", status.HTTP_204_NO_CONTENT) 
        if not validateEmail(data['email']):
            raise serializers.ValidationError("Este email não é válido", status.HTTP_400_BAD_REQUEST)
        if not validateName(data['name']):
            raise serializers.ValidationError("O nome deve conter apenas letras", status.HTTP_400_BAD_REQUEST)
        return data
            
