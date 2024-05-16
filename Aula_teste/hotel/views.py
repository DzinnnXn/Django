from django.shortcuts import render, HttpResponse
from .models import hotel
from .models import quarto
from .models import usuario
from .forms import FormNome

# Create your views here.
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

def reserva(request):
    context = {}
    dados_reserva = quarto.objects.all()
    context["dados_reserva"] = dados_reserva
    return render(request,'reserva.html', context)


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

            print(var_nome)
            print(var_email)

            return HttpResponse("<h1> Login Concluido </h1>")


    else:
        form = FormNome()

    return render(request, "reserva.html", {"form": form})

    