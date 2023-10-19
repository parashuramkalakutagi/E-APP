from rest_framework import serializers
from .models import *

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        # fields = '__all__'
        exclude = ['created_at','updated_at']

class highlightsserializer(serializers.ModelSerializer):
    class Meta:
        model = Highlights
        # fields = '__all__'
        exclude = ['created_at', 'updated_at']


class OtherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Others_Details
        exclude = ['created_at','updated_at']

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptops
        exclude = ['created_at','updated_at']


class MobilessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobiles
        exclude = ['created_at','updated_at']


