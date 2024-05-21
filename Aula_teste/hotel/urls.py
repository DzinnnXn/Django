from django.urls import path
from . import views

urlpatterns = [
     path('', views.homepage, name='homepage'),
    path('quartos/', views.page_quartos, name='page_quartos'),
    path('reserva/', views.reserva, name='reserva'),
    path('mostrar_reservas/', views.mostrar_reservas, name='mostrar_reservas'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('login_error/', views.login_error, name='login_error')
]
