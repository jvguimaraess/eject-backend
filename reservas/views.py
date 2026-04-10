from django.shortcuts import render, redirect
from .forms import ReservaForm


def reservar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReservaForm()
# como não temos uma página de confirmação, redirecionamos para a home após salvar a reserva
    return render(request, 'index.html', {'form': form})