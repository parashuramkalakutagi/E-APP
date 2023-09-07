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
