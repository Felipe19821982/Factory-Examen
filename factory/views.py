# factory/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from .models import Solicitud
from django.contrib.auth.decorators import login_required

def index2(request):
    context = {"clase": "index2"}
    return render(request, 'demo/index2.html', context)

def laboratorio(request):
    context = {"clase": "laboratorio"}
    return render(request, 'demo/laboratorio.html', context)

def home(request):
    return render(request, 'demo/index.html')

def contacto_list(request):
    return render(request, 'demo/contacto_list.html')

# def registrarsolicitud(request):
#     codigo=request.POST['txtCodigo']
#     nombre=request.POST['txtNombre']
#     cantidad=request.POST['numCantidad']

    solicitud = solicitud.objects.create(codigo=codigo, nombre=nombre, cantidad= cantidad)
    return redirect('/')

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




def transbank(request):
    return render(request, 'demo/transbank.html')


def gestionsolicitudes(request):
    solicitud = solicitud.objects.all()
    return render(request, "demo/gestionsolicitudes.html", {"solicitud": solicitud})


# PRUEBA DE VISTAS Y CONEXIONES DE LOGIIN

def index(request):
    context={"clase": "inicio"}
    return render(request, 'demo/index.html', context)


@login_required
def perfil(request):
    context={"clase": "perfil"}
    return render(request, 'demo/perfil.html', context)

def galeria(request):
    users=get_current_users()
    context={"clase": "galeria", "users":users}
    return render(request, 'demo/galeria.html', context)


def registro(request):
    if request.method != "POST":
        context={"clase": "registro"}
        return render(request, 'demo/registro.html', context)
    else:
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(nombre, email, password)
        user.save()
        context={"clase": "registro", "mensaje":"Los datos fueron registrados"}
        return render(request, 'demo/registro.html', context)   
    
def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)