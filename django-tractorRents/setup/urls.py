from django.contrib import admin
from django.urls import path, include
from minasul.views import TractorsViewSet, DriversViewSet, TractorRentViewSet, ListDriverRentsViewSet, ListTractorRentsViewSet
from rest_framework import routers


"""Rota principal padrão do django,
Associando nossas rotas à rota padrão"""
router = routers.DefaultRouter() 
router.register('tractors', TractorsViewSet, basename='Tractors')
router.register('drivers', DriversViewSet, basename='Drivers')
router.register('rents', TractorRentViewSet, basename='All Tractor Rents')



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),  #incluo na rota padrão, as minhas rotas /tractors e /drivers
    path("driver/<int:pk>/rents/", ListDriverRentsViewSet.as_view()),
    path("tractor/<int:id>/drivers/", ListTractorRentsViewSet.as_view())
]
