import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ReservaForm
from .models import Reserva

def reservar(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            form = ReservaForm(dados)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'status': 'erro', 'erros': form.errors}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'erro', 'mensagem': str(e)}, status=400)
    return JsonResponse({'status': 'erro'}, status=405)