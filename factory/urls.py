from django.urls import path # type: ignore
from . import views

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
]
