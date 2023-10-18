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
from .mobile_data_api import phone_details

class LaptopViewset(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        try:
            phone_details()
            response = {
                "message": "data uploded to database ",
                "status_code": HTTP_201_CREATED
            }
            return Response(response,status=HTTP_201_CREATED)
        except KeyError as e:
            response = {
                "error": str(e),
                "message": "Invalid data format.",
                "status_code": HTTP_400_BAD_REQUEST
            }
            return Response(response, status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            response = {
                "error": str(e),
                "message": "Something went wrong.",
                "status_code": HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=HTTP_500_INTERNAL_SERVER_ERROR)

class Laptops_list_view(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        try:
            query = Laptops.objects.all().order_by('?')[0:10]
            sr = LaptopSerializer(query,many=True).data
            return Response(sr)
        except KeyError as e:
            response = {
                "error": str(e),
                "message": "Invalid data format.",
                "status_code": HTTP_400_BAD_REQUEST
            }
            return Response(response, status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            response = {
                "error": str(e),
                "message": "Something went wrong.",
                "status_code": HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=HTTP_500_INTERNAL_SERVER_ERROR)



class MobileViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self,request,*args,**kwargs):
        try:
            queryset = Mobile.objects.all()
            serializers = MobileSerializer(queryset, many=True).data
            return Response(serializers, status=HTTP_200_OK)

        except queryset.DoesNotExist:
            error_message = 'Queryset not found '
            return Response({'message': error_message, 'status_code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error_message = 'Something went wrong.'
            return Response({'message': error_message, 'status_code': status.HTTP_400_BAD_REQUEST, 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


    def create(self,request,*args,**kwargs):
        try:
            data  = request.data
            mobile, _ = Mobile.objects.create(
                brand = Brand.objects.get(brand_name = data.get('brand')),
                catagory = Catagory.objects.get(catagory = data.get('catagory')),
                name = data.get('name'),
                discription = data.get('discription'),
                image = data.get('image'),
                colour = Colour.objects.get(colour = data.get('colour')),
                price = data.get('price'),
                price_off = data.get('price_off'),
                storage = data.get('storage'),
                popularity = data.get('popularity'),
                rating = data.get('rating'),
            )

            responce = {
                'massage':'object created ...',
                'status code': HTTP_201_CREATED,
            }
            return Response(responce,status=HTTP_201_CREATED)

        except Exception as e:
            print(e)
            responce = {
                'massage':'something went wrong...!',
                'status code':HTTP_400_BAD_REQUEST,
                'error':e
            }
            return Response(responce,status=HTTP_400_BAD_REQUEST)



class highlightsViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request,*args,**kwargs):
        try:
            qr = Highlights.objects.all()
            sr = highlightsserializer(qr, many=True)
            return Response(sr.data, status=HTTP_200_OK)

        except qr.DoesNotExist:
            error_message = 'Queryset not found '
            return Response({'message': error_message, 'status_code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error_message = 'Something went wrong.'
            return Response({'message': error_message, 'status_code': status.HTTP_400_BAD_REQUEST, 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            Highlights.objects.create(
                mobile = Mobile.objects.get(uuid = data.get('mobile')),
                ram = data.get('ram'),
                processor = data.get('processor'),
                camera = data.get('camera'),
                front_camera = data.get('front_camera'),
                display = data.get('display'),
                battery = data.get('battery'),
            )
            responce = {
                'massage': 'object created ...',
                'status code': HTTP_201_CREATED,
            }
            return Response(responce, status=HTTP_201_CREATED)

        except Mobile.DoesNotExist:
            error_message = 'Mobile not found with the given UUID.'
            return Response({'message': error_message, 'status_code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error_message = 'Something went wrong.'
            return Response({'message': error_message, 'status_code': status.HTTP_400_BAD_REQUEST, 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class OtherDetailsViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            Others_Details.objects.create(
                mobile = Mobile.objects.get(uuid = data.get('mobile')),
                network = data.get('network'),
                sim_type = data.get('sim_type'),
                expandible_storage = data.get('expandible_storage'),
                audio_jack = data.get('audio_jack'),
                quick_charge = data.get('quick_charge'),
                in_the_box = data.get('in_the_box'),
                warranty = data.get('warranty'),
            )
            responce = {
                'massage': 'object created ...',
                'status code': HTTP_201_CREATED,
            }
            return Response(responce, status=HTTP_201_CREATED)


        except Mobile.DoesNotExist:
            error_message = 'Mobile not found with the given UUID.'
            return Response({'message': error_message, 'status_code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error_message = 'Something went wrong.'
            return Response({'message': error_message, 'status_code': status.HTTP_400_BAD_REQUEST, 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

