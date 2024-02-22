from rest_framework import serializers
from .models import Item, City

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'population', 'latitude', 'longitude', 'region', 'summary')
