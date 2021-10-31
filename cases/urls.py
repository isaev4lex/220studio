from django.urls import path
from . import views

urlpatterns = [
    path('', views.cases, name='cases'),
    path('<slug:category_slug>/', views.cases, name='cases_slug'),
]
