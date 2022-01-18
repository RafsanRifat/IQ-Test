from django.contrib import admin
from django.urls import path, include
from .views import home, iq_test
from django.views.generic import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('test/', iq_test, name='test'),
    path('result/', TemplateView.as_view(template_name='result.html'), name='result'),
]
