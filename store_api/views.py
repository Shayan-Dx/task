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