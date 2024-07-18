from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Solicitud

def index(request):
    return render(request, 'demo/index.html')

def home(request):
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

def registrarse(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'registration/registrarse.html')

def transbank(request):
    return render(request, 'demo/transbank.html')

def gestionsolicitudes(request):
    solicitud = Solicitud.objects.all()
    return render(request, "demo/gestionsolicitudes.html", {"solicitud": solicitud})

def galeria(request):
    return render(request, 'demo/galeria.html')

def registro(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'demo/registro.html')

@login_required
def perfil(request):
    return render(request, 'demo/perfil.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required
def user_crud(request):
    users = User.objects.all()
    return render(request, 'admin/user_crud.html', {'users': users})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_crud')

@login_required
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.username = request.POST['username']
        user.email = request.POST['email']
        if request.POST['password']:
            user.set_password(request.POST['password'])
        user.save()
        return redirect('user_crud')
    return render(request, 'admin/update_user.html', {'user': user})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.utils import timezone
from .models import Solicitud
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'registration/login.html', {'form': form, 'mensaje': 'Credenciales inválidas'})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def registrarse(request):
    if request.method != "POST":
        context={"clase": "registrarse"}
        return render(request, 'demo/registrarse.html', context)
    else:
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(nombre, email, password)
        user.save()
        context={"clase": "registro", "mensaje":"Los datos fueron registrados"}
        return render(request, 'demo/registrarse.html', context)

# Define other views similarly


def logout_view(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.method == "POST":
        username = request.POST["nombre"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "Registration successful.")
        return redirect('login')
    return render(request, 'registration/registro.html')

@login_required
def perfil(request):
    return render(request, 'demo/perfil.html')
