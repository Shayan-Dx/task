from django.shortcuts import render

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    def get(self, request, primary):
        try:
            product = Product.objects.get(pk=primary)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={'request':request})
        return Response(serializer.data)
    
    def put(self, request, primary):
        product = Product.objects.get(pk=primary)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True, context={'request':request})
        return Response(serializer.data)
    

class CategoryDetailView(APIView):
    def get(self, request, primary):
        try:
            category = Category.objects.get(pk=primary)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, context={'request':request})
        return Response(serializer.data)
    
    def put(self, request, primary):
        category = Category.objects.get(pk=primary)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
