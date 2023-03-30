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
