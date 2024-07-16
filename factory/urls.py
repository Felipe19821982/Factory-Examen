# factory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('laboratorio/', views.laboratorio, name='laboratorio'),
    path('contacto_list/', views.contacto_list, name='contacto_list'),
    path('pc_armados/', views.pc_armados, name='pc_armados'),
    path('pc_gamer/', views.pc_gamer, name='pc_gamer'),
    path('workstations/', views.workstations, name='workstations'),
    path('home_office/', views.home_office, name='home_office'),
    path('carrito/', views.carrito, name='carrito'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('transbank/', views.transbank, name='transbank'),
    path('gestionsolicitudes/', views.gestionsolicitudes, name='gestionsolicitudes'),
    # path('registrarsolicitud/', views.registrarsolicitud, name= 'registrarsolicitud' )
    # path('crud', views.crud, name='crud’),

    path('', views.index, name='index'),
    path('galeria', views.galeria, name='galeria'),
    path('registro', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
]
