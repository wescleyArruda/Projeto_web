from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente, Livro, Alugados
from .forms import ClienteForm, LivroForm, AluguelForm


def CadastraCliente(request):
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return mensagem(request)
    else:
        form = ClienteForm()

        dados = {
            "form": form,
        }

        return render(request, "cadastro_cliente.html", dados)

def CadastraLivros(request):
    livros = Livro.objects.all()

    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return mensagem(request)
    else:
        form = LivroForm()

        dados = {
            "form": form,
        }

        return render(request, "cadastro_livros.html", dados)

def CadastraAluguel(request):
    alugueis = Alugados.objects.all()

    if request.method == 'POST':
        form = AluguelForm(request.POST)

        if form.is_valid():
            form.save()
            return mensagem(request)
    else:
        form = AluguelForm()

        dados = {
            "form": form,
        }

        return render(request, "cadastro_aluguel.html", dados)

def mensagem(request):
    return render(request, "mensagem.html")

def ListaLivro(request):
    livros=Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def ListaCliente(request):
    clientes=Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def ListaAlugueis(request):
    alugados = Alugados.objects.all()
    livros = Livro.objects.all()
    clientes = Cliente.objects.all()

    lista_livro= []
    lista_cliente = []

    for i in alugados:
        for j in livros:
            if livros[j] in alugados.alug_livro: 
                for z in clientes:
                    if clientes[z] in alugados.alug_cliente:
                        lista_livro.append(livros[j])
                        lista_cliente.append(clientes[z])

    return render(request, 'lista_alugueis.html', {'alugados':alugados, 'lista_cliente':lista_cliente, 'lista_livro':lista_livro})

def index(request):
    return render(request, "index.html")
