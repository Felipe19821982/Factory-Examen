from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.db import IntegrityError
from .forms import CustomUserCreationForm
from .models import Cliente
from django.contrib.admin.views.decorators import staff_member_required

# Función para verificar si el usuario es "admin"
def admin_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_staff and u.username == 'admin')(view_func))
    return decorated_view_func

# Vistas de la aplicación
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

# Vistas del CRUD de clientes
def gestion_registro(request):
    user_listados = User.objects.all()
    return render(request, "demo/gestionRegistro.html", {"users": user_listados})

@admin_required
def registrar_cliente(request):
    if request.method == "POST":
        codigo = request.POST.get('txtCodigo')
        nombre = request.POST.get('txtNombre')
        apellido = request.POST.get('txtApellido')
        correo = request.POST.get('txtCorreo')

        if not codigo or not nombre or not apellido or not correo:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('registrar_cliente')

        if Cliente.objects.filter(codigo=codigo).exists():
            messages.error(request, "El código ya está en uso.")
            return redirect('registrar_cliente')

        Cliente.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, correo=correo)
        messages.success(request, "Cliente registrado correctamente.")
        return redirect('gestion_registro')
    return render(request, "demo/edicionCliente.html")

@admin_required
def edicion_cliente(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "demo/edicionCliente.html", {"user": user})

@admin_required
def editar_cliente(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = get_object_or_404(User, id=user_id)
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Usuario editado correctamente.")
        return redirect('gestion_registro')


@admin_required
def eliminar_cliente(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "Usuario eliminado correctamente.")
    return redirect('gestion_registro')
