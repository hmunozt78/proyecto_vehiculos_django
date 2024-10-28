from django.shortcuts import render
from django.forms import ValidationError
from django.contrib import messages
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required, permission_required 
from django.views.generic import ListView
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import redirect



# Create your views here.
#LOS DECORADORES SON SOLO PARA FUNCIONES
#@login_required(login_url='/usuarios/login/')
#@permission_required('vehiculo.visualizar_catalogo', raise_exception=False, login_url='/')   
 
class VehiculoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Vehiculo
    template_name = "vehiculo/lista_vehiculos.html"
    context_object_name = 'vehiculos'
    
    permission_required = 'vehiculo.visualizar_catalogo'
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.info(self.request,"Usted no tiene permisos")
            return redirect('home')
        else:
            messages.info(self.request,"Primero debe identificarse")
            return redirect('login')

@login_required(login_url='/usuarios/login/')
@permission_required('vehiculo.add_vehiculo', raise_exception=False, login_url='/')
def registro(request):
    #return render(request, "vehiculo/registro_vehiculo.html", {})
    if request.method == 'POST':
        # LÓGICA PARA PROCESAR LOS DATOS Y GUARDARLOS
        form = VehiculoForm(request.POST)
        
        if form.is_valid():
            try:
                vehiculo = form.save(commit=False)
                vehiculo.clean() # váldamos que cumpla con las restricciones del modelo
                vehiculo.save() # guardamos los datos del modelo
                messages.success(request, "producto creado correctamente.")
            
            except ValidationError as e:
                messages.error(request, e.messages)
        else:
            messages.error(request, "Error al intentar crear el producto, intente nuevamente.")
        
        return render(request, "vehiculo/registro_vehiculo.html", {"form": VehiculoForm()})
    
    else:
        form = VehiculoForm()
        return render(request, "vehiculo/registro_vehiculo.html", {"form": form})


