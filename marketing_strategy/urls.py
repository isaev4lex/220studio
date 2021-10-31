from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketing_strategy, name='marketing-strategy'),
]
