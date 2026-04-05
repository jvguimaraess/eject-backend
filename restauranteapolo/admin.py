from django.contrib import admin
from .models import Artigo
from .models import Funcionario
from .models import destaque

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data')
    search_fields = ('titulo', 'autor')
    list_filter = ('data', 'autor')
    ordering = ('-titulo', '-data')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')
    search_fields = ('nome', 'cargo')
    list_filter = ('cargo',)
    ordering = ('-nome',)

@admin.register(destaque)
class destaqueAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)
    ordering = ('-titulo',)