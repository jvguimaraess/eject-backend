from django.contrib import admin
from .models import Autor, Artigo, MembroEquipe, Destaque, Servico

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data')
    search_fields = ('titulo',)
    list_filter = ('data', 'autor')
    ordering = ('-data',)

@admin.register(MembroEquipe)
class MembroEquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')
    search_fields = ('nome', 'cargo')
    list_filter = ('cargo',)

@admin.register(Destaque)
class DestaqueAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)