from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.views import get_schema_view

from drf_yasg import openapi

from rest_framework import permissions

from .views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, ProductCreate, CategoryCreate


schema_view = get_schema_view(
    openapi.Info(
        title="Store API",
        default_version='Version 1.0.0',
        description="API documentation",
        contact=openapi.Contact(email="shayanvafi0@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    # permission_classes=(permissions.IsAuthenticated,),
    # authentication_classes=(JWTAuthentication,),
)


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:primary>/', ProductDetailView.as_view()),
    path('products/add/', ProductCreate.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:primary>/', CategoryDetailView.as_view()),
    path('categories/add/', CategoryCreate.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]