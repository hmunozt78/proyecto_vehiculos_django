from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
#from .. import vehiculo
from django.contrib.auth.models import Permission


# Create your views here.

# def login(request):
#     return render(request, "usuarios/login.html", {})

# def reg_usuario(request):
#     return render(request, "usuarios/reg_usuarios.html", {})

class UserLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login Exitoso')
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return self.get_redirect_url() or self.success_url
    
class UserLogoutView(LogoutView):
    next_page = 'home'
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Has Cerrado la sesion')
        return super().dispatch(request, *args, **kwargs)
    
    
class UserRegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'usuarios/reg_usuarios.html'
    success_url = reverse_lazy('login')
    
    
    ##
    ##
    ##  AQUI DEBO REVISAR COMO AGREGAR LOS PERMISOS AL CREAR EL USUARIO
    ##
    ##
    ##
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        
        permiso = Permission.objects.get(codename= 'visualizar_catalogo', content_type__app_label='vehiculo')
            
        user.user_permissions.add(permiso)        
        messages.success(self.request, 'Registro realizo con exito.')
        return super().form_valid(form)
        
