from django.forms import ModelForm
from .models import *


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

class AluguelForm(ModelForm):
    class Meta:
        model = Alugados
        fields = '__all__'
