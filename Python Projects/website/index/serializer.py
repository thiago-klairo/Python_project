from rest_framework import serializers
from index.models import Fruits, Region

class regionSerializer(serializers.ModelSerializer):
 class Meta:
     model = Region
     fields = ['id', 'name']



class fruitsSerializer(serializers.ModelSerializer):
 class Meta:
     model = Fruits
     fields = ['id', 'name', 'match']     