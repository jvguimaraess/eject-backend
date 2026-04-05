from django.db import models

#Tipos de estados para a reserva.
STATUS_CHOICES = [
    ('P', 'Pendente'),
    ('C', 'Confirmada'),
    ('X', 'Cancelada'),
]
class Reserva(models.Model):
    #Campos
    nome_cliente = models.CharField(max_length=100)
    data_reserva = models.DateField()
    hora_reserva = models.TimeField()
    numero_pessoas = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    #Representação da string do modelo.
    def __str__(self):
        return f"{self.nome_cliente} - {self.data_reserva} {self.hora_reserva}"    
