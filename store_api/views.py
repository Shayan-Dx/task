from django.shortcuts import render
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .authentication import SafeJWTAuthentication

from apikey.throttling import ExceptionalUserRateThrottle

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = settings.PAGINATION_PAGE_SIZE
    page_size_query_param = settings.PAGINATION_PAGE_SIZE_QUERY_PARAM
    max_page_size = settings.PAGINATION_MAX_PAGE_SIZE


class ProductListView(APIView):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    throttle_classes = [ExceptionalUserRateThrottle]
    authentication_classes = [SafeJWTAuthentication]

    # @method_decorator(cache_page(120))
    def get(self, request):
        products = Product.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            products = products.filter(title__icontains=title)
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True, context={'request':request})
        return paginator.get_paginated_response(serializer.data)


class ProductDetailView(APIView):

    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, primary):
        try:
            product = Product.objects.get(pk=primary)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={'request':request})
        return Response(serializer.data)
    
    
    def put(self, request, primary):
        try:
            product = Product.objects.get(pk=primary)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, primary):
        try:
            product = Product.objects.get(pk=primary)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

class ProductCreate(APIView):

    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryListView(APIView):

    pagination_class = CustomPagination    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    @method_decorator(cache_page(120))
    def get(self, request):
        categories = Category.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            categories = categories.filter(title__icontains=title)
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(result_page, many=True, context={'request':request})
        return paginator.get_paginated_response(serializer.data)


class CategoryDetailView(APIView):

    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, primary):
        try:
            category = Category.objects.get(pk=primary)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, context={'request':request})
        return Response(serializer.data)
    
    def put(self, request, primary):
        try:
            category = Category.objects.get(pk=primary)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, primary):
        try:
            category = Category.objects.get(pk=primary)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

class CategoryCreate(APIView):

    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)