from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
home = DefaultRouter()

home.register('MobileViewset',MobileViewset,basename='MobileViewset')
home.register('highlightsViewset',highlightsViewset,basename='highlightsViewset')
home.register('OtherDetailsViewset',OtherDetailsViewset,basename='OtherDetailsViewset')

urlpatterns = [
    path('',include(home.urls)),
]