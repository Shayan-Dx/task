from rest_framework.throttling import UserRateThrottle
from pytimeparse.timeparse import timeparse
from rest_framework_simplejwt.state import token_backend
from ipaddress import ip_address, ip_network
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from store_api.authentication import SafeJWTAuthentication
from apikey.models import APIKey

class ExceptionalUserRateThrottle(UserRateThrottle):
    def allow_request(self, request, view):
        try:
            user = SafeJWTAuthentication().authenticate(request)[0]
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            ip = request.META.get("REMOTE_ADDR")
            request.user = user
        except:
            return True
        
        try:
            decoded_token = token_backend.decode(token, verify=True)
            key = decoded_token.get('APIKey', None)
        except:
            key = None
        
        if key is None:
            return True
        
        try:
            api_key = APIKey.objects.get(refresh=token)
        except:
            raise ValidationError(_("Your Token is not accepted"))
        
        for reqIp in api_key.source_ips['ips']:
            if ip_address(ip) in ip_network(reqIp):
                self.key = self.get_cache_key(request, view)
                if self.key is None:
                    return True
                
                self.history = self.cache.get(self.key, [])
                self.now = self.timer()
                override_rate = api_key.usage_rate
                if override_rate is not None:
                    self.num_requests, self.duration = self.parse_rate(override_rate)
                while self.history and self.history[-1] <= self.now - self.duration:
                    self.history.pop()
                if len(self.history) >= self.num_requests:
                    return self.throttle_failure()
                return self.throttle_success()
        
        raise ValidationError("Your ip address is not accepted")
    
    def parse_rate(self, rate):
        if rate is None:
            return (None, None)
        num, period, unit = rate.split('/')
        num_requests = int(num)
        duration = timeparse(period + unit)
        return (num_requests, duration)