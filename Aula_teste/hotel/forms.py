from django import forms


class FormNome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20)
    sobrenome = forms.CharField(label='Sobrenome', max_length=20)
    email = forms.EmailField(label='Email', max_length=100)
    idade = forms.IntegerField(label='Idade', min_value=0, max_value=100)
    endereco = forms.CharField(label='Endereco', max_length=200)
    QUARTOS = [
        ('solteiro', 'Quarto Solteiro'),
        ('casal', 'Quarto Casal'),
        ('conforto', 'Quarto Conforto'),
        ('luxo', 'Quarto Luxo')
    ]
    quarto_de_escolha = forms.ChoiceField(choices=QUARTOS, label='Quarto de escolha')
    data_da_reserva = forms.DateField(widget=forms.SelectDateWidget, label='Data da reserva')



