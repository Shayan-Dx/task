"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
   openapi.Info(
      title="Store API",
      default_version='v1.0.0',
      description="You can use this WebPage to access APIs faster and better",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shayanvafi0@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=False,
   permission_classes=(IsAuthenticated,IsAdminUser),
   authentication_classes=(JWTAuthentication,),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store_api.urls')),
    path('', include('apikey.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
