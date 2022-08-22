from dataclasses import dataclass
from time import timezone
from tkinter import CASCADE
from django.db import models
from django.forms import DateTimeField


# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome do cliente', max_length=250)
    cpf = models.FloatField('CPF')

    def __str__(self):
        return str(self.nome)


class Livro(models.Model):
    titulo = models.CharField('Titulo', max_length=250)
    ano = models.IntegerField('Ano de lancamento')
    autor = models.CharField('Autor', max_length=250)

    def __str__(self):
        return str(self.titulo)

class Alugados(models.Model):
    alug_livro= models.ForeignKey(Livro, on_delete=models.CASCADE)
    alug_cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_do_aluguel = models.DateTimeField()

    def __str__(self):
        return str(self.alug_livro)

