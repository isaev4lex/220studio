from django.urls import path
from . import views

urlpatterns = [
    path('', views.logo_and_style, name='logo-and-style'),
]
