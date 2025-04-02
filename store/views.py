from .models import Category, Products
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import categorySerializer, productSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required





class CategoryListAPI(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = categorySerializer(categories, many=True)
        return Response(serializer.data)
    

class ProductListAPI(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
    

class ProductDetailsAPI(APIView):
    def get(self, request, product_ID):
        try:
            product = Products.objects.get(id=product_ID)
            serializer = productSerializer(product)
            return Response(serializer.data)
        except Products.DoesNotExist:
            return Response({'error': 'Product with this id does not exist'}, status=404)
        
class ProductByCategory(APIView):
    def get(self, request, category_id):
        sort_order = request.query_params.get('sort', 'asc')
        if sort_order == 'desc':
            products = Products.objects.filter(category_id = category_id).order_by('-price')
        else:
            products = Products.objects.filter(category_id=category_id).order_by('price')

        if not products.exists():
            return Response({'error': 'No products found for this category'}, status=404)
        
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)


class ProductSearchAPI(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        products = Products.objects.filter(
            name__icontains=query
        ) | Products.objects.filter(
            details__icontains=query
        ) | Products.objects.filter(
            tags__icontains=query
        )
        

        if not products.exists():
            return Response({'error': 'No products found'}, status=404)
        
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
    


