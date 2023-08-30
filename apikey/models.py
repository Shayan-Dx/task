from django.db import models
from django.contrib.auth.models import User


class APIKey(models.Model):
    user = models.ForeignKey(User ,max_length=50, on_delete=models.CASCADE)
    expire_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username