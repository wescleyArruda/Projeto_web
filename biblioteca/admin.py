from django.contrib import admin
from .models import Cliente,Livro,Alugados

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'cpf')

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo','ano','autor')


@admin.register(Alugados)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('alug_livro','alug_cliente','data_do_aluguel')
