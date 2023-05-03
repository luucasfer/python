from django.db import models
from tractorsApp.validators import *
from django.forms import forms

"""Modelos das tabelas, assim como no peewee """

class Tractor(models.Model):
    identification  = models.CharField(max_length=30, null=True, unique=True, blank=False)
    owner           = models.CharField(max_length=50, blank=False)
    tractorYear     = models.CharField(max_length=4)
    manufacter      = models.CharField(max_length=30)
    lastReview      = models.DateField(null=True)
    lastLocation    = models.CharField(max_length=100)
    lastFuelDate    = models.DateField()
    
    def __str__(self):
        return self.identification
    

class Driver(models.Model):
    GENDER = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'Not informed'))

    name            = models.CharField(max_length=50, blank=False)
    birthYear       = models.DateField()
    cpf             = models.CharField(max_length=11, unique=True, blank=False)
    cnh             = models.CharField(max_length=11, unique=True, blank=False)
    gender          = models.CharField(max_length=1, choices=GENDER, blank=False, null=False, default='X')

    def __str__(self):
        return self.name


class TractorRent(models.Model):
    tractor       = models.ForeignKey(Tractor, on_delete=models.RESTRICT)
    driver        = models.ForeignKey(Driver, on_delete=models.RESTRICT)
    date          = models.DateField()




# class Tools(models.Model):
#     toolName    = models.CharField(max_length=50)
#     model       = models.CharField(max_length=20)
#     atStock   = models.BooleanField()
#     borrowedTo  = models.ForeignKey()

#     def __str__(self):
#         return self.toolName

