from django.db import models
from adopet.validators import *



class Tutor(models.Model):
    name        = models.CharField(max_length=30,  null=True,  blank=False, unique=True)
    email       = models.CharField(max_length=50,  null=True,  blank=False, unique=True)
    password    = models.CharField(max_length=4,   null=True,  blank=False)
    phone       = models.CharField(max_length=30,  null=False, blank=True)
    city        = models.CharField(max_length=30,  null=False, blank=True)
    about       = models.CharField(max_length=250, null=False, blank=True)
    
    def __str__(self):
        return self.name


class Abrigo(models.Model):
    name        = models.CharField(max_length=30,  null=True,  blank=False, unique=True)
    phone       = models.CharField(max_length=15,  null=False, blank=False)
    city        = models.CharField(max_length=30,  null=False, blank=False)
    state       = models.CharField(max_length=2,   null=False, blank=False)
    
    def __str__(self):
        return self.name


class Pet(models.Model):
    abrigo          = models.ForeignKey(Abrigo, on_delete=models.RESTRICT)
    name            = models.CharField(max_length=30,  null=True,  blank=False)
    age             = models.CharField(max_length=15,  null=False, blank=True)
    size            = models.CharField(max_length=15,  null=False, blank=True)
    caracteristic   = models.CharField(max_length=50,  null=False, blank=True)
    adopted         = models.BooleanField(default=False)
    #address        = models.ForeignKey(Abrigo, on_delete=models.RESTRICT)
    image           = models.ImageField()
    
    def __str__(self):
        return self.name
