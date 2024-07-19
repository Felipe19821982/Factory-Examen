# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.db import IntegrityError
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'demo/index.html')

def laboratorio(request):
    return render(request, 'demo/laboratorio.html')

def contacto_list(request):
    return render(request, 'demo/contacto_list.html')

def pc_armados(request):
    return render(request, 'demo/pc_armados.html')

def pc_gamer(request):
    return render(request, 'demo/pc_gamer.html')

def workstations(request):
    return render(request, 'demo/workstations.html')

def home_office(request):
    return render(request, 'demo/home_office.html')

def carrito(request):
    return render(request, 'demo/carrito.html')

def transbank(request):
    return render(request, 'demo/transbank.html')

def gestionsolicitudes(request):
    return render(request, 'demo/gestionsolicitudes.html')

def galeria(request):
    return render(request, 'demo/galeria.html')

def registro(request):
    if request.user.is_authenticated:
        logout(request)
    
    Session.objects.filter(expire_date__lte=timezone.now()).delete()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Usuario registrado correctamente. Por favor, inicia sesión.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'El nombre de usuario o el correo electrónico ya están en uso.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registrarse.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'registration/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Sesión cerrada correctamente')
        return redirect('index')
    else:
        return redirect('index')

@login_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required
def user_crud(request):
    users = User.objects.all()
    return render(request, 'admin/user_crud.html', {'users': users})

@login_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('user_crud')

@login_required
def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user.username = username
        user.email = email
        user.save()
        return redirect('user_crud')
    return render(request, 'admin/update_user.html', {'user': user})

# PRUEBA DE REGISTRO
def registrate(request):
    if request.method != "POST":
        context = {"clase": "registrate"}
        return render(request, 'demo/registrate.html', context)
    else:
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not nombre or not email or not password:
            context = {"clase": "registrate", "mensaje": "Todos los campos son obligatorios."}
            return render(request, 'demo/registrate.html', context)
        try:
            user = User.objects.create_user(username=nombre, email=email, password=password)
            user.save()
            context = {"clase": "registrate", "mensaje": "Los datos fueron registrados"}
        except IntegrityError:
            context = {"clase": "registrate", "mensaje": "El nombre de usuario o el correo electrónico ya están en uso."}
        return render(request, 'demo/registrate.html', context)

# PRUEBA DE MUESTRA DE LOGIN
class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
