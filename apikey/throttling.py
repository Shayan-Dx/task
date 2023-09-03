from rest_framework.throttling import UserRateThrottle
from rest_framework_simplejwt.state import token_backend
from rest_framework.exceptions import ValidationError

from django.conf import settings

import jwt

from pytimeparse.timeparse import timeparse

from store_api.authentication import SafeJWTAuthentication

from apikey.models import APIKey


class ExceptionalUserRateThrottle(UserRateThrottle):
    def allow_request(self, request, view):
        try:
            user = SafeJWTAuthentication().authenticate(request)[0]
            token = request.META.get('HTTP_AUTHORIZATION'," ").split(' ')[1]
            request.user = user
        except:
            return True
        
        try:
            decoded_token = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"], verify=True)
            key = decoded_token.get('type', None)
        except:
            key = None

        if key is None and key != "api_key":
            return True
        
        try:
            api_key = APIKey.objects.get(token=token)
        except:
            raise ValidationError("Your Token is not accepted")
        
        self.key = self.get_cache_key(request, view)
        if self.key is None:
            return True
        
                
        self.history = self.cache.get(self.key, [])
        self.now = self.timer()
        throttle_rate = api_key.roll
        if throttle_rate is not None:
            self.num_requests, self.duration = self.parse_rate(throttle_rate)
        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()
        if len(self.history) >= self.num_requests:
            return self.throttle_failure()
        return self.throttle_success()


    def parse_rate(self, rate):
        if rate is None:
            return (None, None)
        num, period , unit = rate.split('/')
        num_requests = int(num) 
        duration = timeparse(period + unit)
        return (num_requests, duration)