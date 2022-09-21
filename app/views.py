from django.shortcuts import render
from .models import Usuarios

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def administrador(request): 
    return render(request, 'app/administrador.html')

def PanelControl(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'app/PanelControl.html', {"Usuarios": usuarios})

def funcionario(request):
    return render(request, 'app/funcionario.html')
