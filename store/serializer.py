from rest_framework import serializers
from .models import Category, Products

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products 
        fields = "__all__"