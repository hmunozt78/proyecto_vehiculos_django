from django.urls import path
from . import views
from .views import VehiculoListView


print("VehiculoListView:", VehiculoListView)  # Agrega esto para diagnóstico

urlpatterns = [
    path('add/', views.registro, name="registro"),
    path('listado/', VehiculoListView.as_view(), name="listado"),
]