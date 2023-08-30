from django.conf import settings
from django.shortcuts import render

from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import APIKeySerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class APIKeyView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        serializer = APIKeySerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            error_message = "Please check your data and try again later!"
            return Response(serializer.errors)