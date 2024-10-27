from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('reg_usuario/', views.UserRegistroView.as_view(), name="reg_usuario"),
    path('salida/', views.UserLogoutView.as_view(), name="salida"),
]