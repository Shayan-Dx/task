from .models import APIKey
from datetime import datetime

import jwt

from rest_framework import serializers

from rest_framework_simplejwt.state import token_backend

from django.conf import settings


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = '__all__'
        extera_kwargs = {
            "token": "read_only"
        }

    def generate_token(self, validated_data:dict):
        user = validated_data.get("user")
        expire_time = validated_data.get("expire_time")
        payload = {
            "type": "api_key",
            "user_id": user.id,
            "exp":expire_time,
        }

        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")
        return token

    def validate(self, attrs):
        user = attrs.get("user")
        expire_time = attrs.get("expire_time")
        is_active = attrs.get("is_active")
        roll = attrs.get("roll")
        token = self.generate_token(attrs)

        APIKey.objects.create(
            user=user,
            expire_time=expire_time,
            is_active=is_active,
            roll = roll,
            token=token
        )

        return attrs