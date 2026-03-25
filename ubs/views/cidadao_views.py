from django.shortcuts import render, redirect, get_object_or_404
from ..models import Cidadao
from ..forms import CidadaoForm


def create_cidadao(request):
    form = CidadaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_cidadao')
    return render(request, 'cidadao/create.html', {'form': form})


def list_cidadao(request):
    data = Cidadao.objects.select_related('pessoa', 'address', 'ubs').all()
    return render(request, 'cidadao/list.html', {'cidadaos': data})


def detail_cidadao(request, id):
    obj = get_object_or_404(Cidadao, id=id)
    return render(request, 'cidadao/detail.html', {'obj': obj})


def update_cidadao(request, id):
    obj = get_object_or_404(Cidadao, id=id)
    form = CidadaoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_cidadao')
    return render(request, 'cidadao/update.html', {'form': form})


def delete_cidadao(request, id):
    obj = get_object_or_404(Cidadao, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_cidadao')
    return render(request, 'cidadao/delete.html', {'obj': obj})