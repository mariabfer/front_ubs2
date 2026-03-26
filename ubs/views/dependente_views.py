from django.shortcuts import render, redirect, get_object_or_404
from ..models import Dependente
from ..forms import DependenteForm


def create_dependente(request):
    form = DependenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_dependente')
    return render(request, 'ubs/dependente/create.html', {'form': form})


def list_dependente(request):
    data = Dependente.objects.select_related('responsavel', 'dependente').all()
    return render(request, 'ubs/dependente/list.html', {'dependentes': data})


def detail_dependente(request, id):
    dependente = get_object_or_404(Dependente, id=id)
    return render(request, 'ubs/dependente/detail.html', {'dependente': dependente})


def update_dependente(request, id):
    obj = get_object_or_404(Dependente, id=id)
    form = DependenteForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_dependente')
    return render(request, 'ubs/dependente/update.html', {'form': form})


