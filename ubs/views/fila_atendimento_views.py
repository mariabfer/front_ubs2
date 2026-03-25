from django.shortcuts import render, redirect, get_object_or_404
from ..models import Fila_atendimento
from ..forms import FilaForm


def create_fila(request):
    form = FilaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_fila')
    return render(request, 'fila/create.html', {'form': form})


def list_fila(request):
    filas = Fila_atendimento.objects.select_related('ubs', 'medico').all()
    return render(request, 'fila/list.html', {'filas': filas})


def detail_fila(request, id):
    obj = get_object_or_404(Fila_atendimento, id=id)
    return render(request, 'fila/detail.html', {'obj': obj})


def update_fila(request, id):
    obj = get_object_or_404(Fila_atendimento, id=id)
    form = FilaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_fila')
    return render(request, 'fila/update.html', {'form': form})


def delete_fila(request, id):
    obj = get_object_or_404(Fila_atendimento, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_fila')
    return render(request, 'fila/delete.html', {'obj': obj})