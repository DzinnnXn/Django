from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='/'),
    path('quartos', views.page_quartos, name='page_quartos'),
    path('reserva', views.reserva, name="reserva"),
    path('mostrar_reservas', views.mostrar_reservas, name="mostrar_reservas"),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login' )
]
