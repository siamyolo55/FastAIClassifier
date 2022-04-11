# dependencies
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mcc)
]

