from django.contrib import admin
from django.urls import path, include
from .views import home, iq_test

urlpatterns = [
    path('', home, name='home'),
    path('test/', iq_test, name='test'),
    # path('api/', iq_api, name='api'),
]
