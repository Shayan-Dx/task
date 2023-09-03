from django.db import models
from django.contrib.auth.models import User


class APIKey(models.Model):
    user = models.ForeignKey(User ,max_length=50, on_delete=models.CASCADE)
    expire_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, blank=True)
    roll = models.CharField(max_length=55, blank=True)
    def __str__(self):
        return self.user.username
    

# THIS IS AN EXAMPLE FOR GENERATING APIKEY USE WITH CAUTION
# {
#     "user" : 1,
#     "expire_time" : "2024-9-3 12:00:00",
#     "is_active" : true,
#     "roll" : "3/1/minute"
# }