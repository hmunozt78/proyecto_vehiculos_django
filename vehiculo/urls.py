from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.registro, name="registro"),
    path('listado/', views.registro, name="listado"),
]