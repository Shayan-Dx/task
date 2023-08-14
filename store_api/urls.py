from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, ProductCreate, CategoryCreate


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