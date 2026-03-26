from django.shortcuts import render, redirect, get_object_or_404
from ..models import FilaAtendimento
from ..forms import FilaForm


def create_fila(request):
    form = FilaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_fila')
    return render(request, 'ubs/fila/create.html', {'form': form})


def list_fila(request):
    filas = FilaAtendimento.objects.select_related('ubs', 'medico').all()
    return render(request, 'ubs/fila/list.html', {'filas': filas})


def detail_fila(request, id):
    fila = get_object_or_404(FilaAtendimento, id=id)
    return render(request, 'ubs/fila/detail.html', {'fila': fila})


def update_fila(request, id):
    obj = get_object_or_404(FilaAtendimento, id=id)
    form = FilaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_fila')
    return render(request, 'ubs/fila/update.html', {'form': form})


def delete_fila(request, id):
    obj = get_object_or_404(FilaAtendimento, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_fila')
    return render(request, 'ubs/fila/delete.html', {'obj': obj})