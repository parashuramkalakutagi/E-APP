from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
home = DefaultRouter()

home.register('MobileViewset',MobileViewset,basename='MobileViewset')
home.register('highlightsViewset',highlightsViewset,basename='highlightsViewset')
home.register('OtherDetailsViewset',OtherDetailsViewset,basename='OtherDetailsViewset')
home.register('LaptopViewset',LaptopViewset,basename='LaptopViewset')
home.register('Laptops_list_view',Laptops_list_view,basename='Laptops_list_view')
home.register('Oneplus_mobiles_view',Oneplus_mobiles_view,basename='Oneplus_mobiles_view')

urlpatterns = [
    path('',include(home.urls)),
]