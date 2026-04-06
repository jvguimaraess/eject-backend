from django.contrib import admin
from .models import Artigo, MembroEquipe, Destaque

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data')
    search_fields = ('titulo', 'autor')
    list_filter = ('data',)
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