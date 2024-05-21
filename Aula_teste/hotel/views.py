from django.shortcuts import render, redirect, HttpResponse
from .models import hotel
from .models import quarto
from .models import usuario
from .forms import FormNome, FormCadastro, FormLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def reserva(request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_sobrenome = form.cleaned_data['sobrenome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_endereco = form.cleaned_data['endereco']
            var_quarto_de_escolha = form.cleaned_data['quarto_de_escolha']
            var_data_da_reserva = form.cleaned_data['data_da_reserva']

            user = usuario(nome=var_nome, sobrenome=var_sobrenome, email=var_email, idade=var_idade, endereco=var_endereco, quarto_escolha=var_quarto_de_escolha, data_reserva=var_data_da_reserva)
            user.save()

            return redirect('mostrar_reservas')

    else:
        form = FormNome()
    return render(request, 'reserva.html', {'form': form})

def mostrar_reservas(request):
    reservas = usuario.objects.all()  
    return render(request, 'mostrar_reservas.html', {'reservas': reservas})

def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request,'homepage.html', context)

def page_quartos(request):
    context = {}
    dados_quartos = quarto.objects.all()
    context["dados_quartos"] = dados_quartos
    return render(request,'quartos.html', context)

def cadastro(request):
    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']

            user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()

            return HttpResponse('<h1>Foi</h1>')

    else:
        form = FormCadastro()
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            var_user = form.cleaned_data['user']
            var_password = form.cleaned_data['password']

            user = authenticate(username=var_user, password=var_password)
            if user is not None:
                return HttpResponse("<h1>Deu Certo</h1>")
            else:
                return HttpResponse("<h1>Login ou Senha Inválidos<h1>")

          
            return HttpResponse('<h1>Foi</h1>')
    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})

