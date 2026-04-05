from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva

        fields = ['nome_cliente', 'data_reserva', 'hora_reserva', 'numero_pessoas']

        #Configurações do formulário com classes CSS (Genéricas, ainda não definidas) e placeholders.
        widgets = {
            'nome_cliente': forms.TextInput(
                attrs={
                    'class': 'CLASSENOFRONT', 
                    'placeholder': 'Digite seu nome'
                }
            ),
            'data_reserva': forms.DateInput(
                attrs={
                    'class': 'CLASSENOFRONT', 
                    'type': 'date'
                }
            ),
            'hora_reserva': forms.TimeInput(
                attrs={
                    'class': 'CLASSNOFRONT', 
                    'type': 'time'
                }
            ),
            'numero_pessoas': forms.Select(
                attrs={
                    'class': 'CLASSNOFRONT'
                }
            ),
        }