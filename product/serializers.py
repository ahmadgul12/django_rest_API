from dataclasses import field
from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=200)
    Description=serializers.CharField(max_length=200)
    price=serializers.FloatField()

    class Meta:
        model=product
        field=('_all_')