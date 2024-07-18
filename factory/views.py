from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrarse.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
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
        context={"clase": "registrate"}
        return render(request, 'demo/registrate.html', context)
    else:
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(nombre, email, password)
        user.save()
        context={"clase": "registrate", "mensaje":"Los datos fueron registrados"}
        return render(request, 'demo/registrate.html', context)