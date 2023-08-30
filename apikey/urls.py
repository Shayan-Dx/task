from django.urls import path

from .views import APIKeyView

urlpatterns = [
    path('apikey/', APIKeyView.as_view()),
]