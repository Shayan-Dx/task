from .models import APIKey

import jwt

from rest_framework import serializers

from django.conf import settings


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = '__all__'

    def generate_key(self, validated_data:dict):
        user = validated_data.get("user")
        expire_time = validated_data.get("expire_time")
        if user is None:
            raise serializers.ValidationError("User object is None.")
        payload = {
            "type" : "api_key",
            "user_id": user.id,
            "exp": expire_time,
        }

        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")
        return token

    
    def validate(self, attrs):
        user = attrs.get("user")
        expire_time = attrs.get("expire_time")
        is_active = attrs.get("is_active")
        token = self.generate_key(attrs)

        APIKey.objects.create(
            user = user,
            expire_time = expire_time,
            is_active = is_active,
            token = token,
        )

        return attrs