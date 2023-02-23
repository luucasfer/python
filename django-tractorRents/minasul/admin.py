from django.contrib import admin
from minasul.models import Tractor, Driver, TractorRent


class Tractors(admin.ModelAdmin):
    list_display = ('id', 'identification', 'owner', 'tractorYear', 'manufacter', 'lastReview', 'lastLocation', 'lastFuelDate') #campos para mostrar na tela de admin
    list_display_links = ('lastReview', 'lastLocation') #campos que posso editar
    search_fields = ('id', 'identification', 'owner') #campos que posso buscar
    list_per_page = 20  

admin.site.register(Tractor, Tractors)  #(Modelo, ConfiguracaoAdmin)


class Drivers(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthYear', 'cpf', 'cnh', 'gender')
    list_display_links = ('cpf', 'cnh')
    search_fields = ('id', 'name', 'cpf')

admin.site.register(Driver, Drivers)


class TractorRents(admin.ModelAdmin):
    list_display = ('id', 'tractor', 'driver', 'date')
    list_display_links = ('id',)

admin.site.register(TractorRent, TractorRents)