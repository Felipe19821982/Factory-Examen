# urls.py
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('laboratorio/', views.laboratorio, name='laboratorio'),
    path('contacto_list/', views.contacto_list, name='contacto_list'),
    path('pc_armados/', views.pc_armados, name='pc_armados'),
    path('pc_gamer/', views.pc_gamer, name='pc_gamer'),
    path('workstations/', views.workstations, name='workstations'),
    path('home_office/', views.home_office, name='home_office'),
    path('carrito/', views.carrito, name='carrito'),
    path('registrarse/', views.registro, name='registrarse'),
    path('transbank/', views.transbank, name='transbank'),
    path('gestionsolicitudes/', views.gestionsolicitudes, name='gestionsolicitudes'),
    path('galeria/', views.galeria, name='galeria'),
    path('registrate/', views.registrate, name='registrate'),
    
    # Rutas para autenticación y CRUD de usuarios
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/crud/', views.user_crud, name='user_crud'),
    path('admin/crud/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin/crud/update/<int:user_id>/', views.update_user, name='update_user'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Prueba de muestra de login
    path('gestion_registro/', views.gestion_registro, name='gestion_registro'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('edicion_cliente/<int:user_id>/', views.edicion_cliente, name='edicion_cliente'),
    path('editar_cliente/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:user_id>/', views.eliminar_cliente, name='eliminar_cliente'),
]

