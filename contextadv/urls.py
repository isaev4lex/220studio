from django.urls import path
from . import views

urlpatterns = [
    path('', views.contextadv, name='contextadv'),
]
