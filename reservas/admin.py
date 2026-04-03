from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
# Configurações personalizadas para a interface de admin sobre o modelo reserva
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'data_reserva', 'hora_reserva', 'numero_pessoas', 'status')
    list_filter = ('status', 'data_reserva')
    search_fields = ('nome_cliente',)
    ordering = ('data_reserva', 'hora_reserva')
