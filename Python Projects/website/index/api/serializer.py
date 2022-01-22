from rest_framework import serializers
from index import models

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ("id", "name")

class SerializerFruits(serializers.ModelSerializer):
            class Meta:
                model= models.Fruits
                fields = ("id", "name", "match")


