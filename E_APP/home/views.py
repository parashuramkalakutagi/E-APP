from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly
from .models import *
from .serializer import *
from rest_framework.status import *
from django.db.models import Count
from rest_framework import generics
from rest_framework.filters import SearchFilter
from  django.db.models import Count,Max,Min,Avg,Sum,SET
from django.db.models import Q , F
from datetime import timedelta
from django.utils import timezone
import datetime


class MobileViewset(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class highlightsViewset(viewsets.ModelViewSet):
    queryset = Highlights.objects.all()
    serializer_class = highlightsserializer