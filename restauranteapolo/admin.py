from django.contrib import admin
from .models import Autor, Artigo, MembroEquipe, Destaque, Servico

admin.site.register(Autor)
admin.site.register(Artigo)
admin.site.register(MembroEquipe)
admin.site.register(Destaque)
admin.site.register(Servico)