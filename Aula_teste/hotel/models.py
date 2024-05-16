from django.db import models
from datetime import date

# Create your models here.
TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORTO", "Conforto"),
    ("LUXO", "Luxo")
)

class hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.titulo

class quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=255)
    foto_quarto = models.ImageField(upload_to="Foto_Quarto/")

    def __str__(self):
        return self.tipo
    
class usuario(models.Model):
    nome = models.CharField(max_length=20, default='')
    sobrenome = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=50, default='')
    idade = models.IntegerField(default=18)
    endereco = models.CharField(max_length=100, default='')
    quarto_escolha = models.CharField(max_length=50, default='')
    data_reserva = models.DateField(default=date.today)


    def __str__(self):
        return self.nome