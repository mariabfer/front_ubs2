from django.shortcuts import render, redirect, get_object_or_404
from ..models import Telefone
from ..forms import TelefoneForm


def create_telefone(request):
    form = TelefoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_telefone')
    return render(request, 'ubs/telefone/create.html', {'form': form})


def list_telefone(request):
    data = Telefone.objects.select_related('pessoa', 'ubs').all()
    return render(request, 'ubs/telefone/list.html', {'telefones': data})


def detail_telefone(request, id):
    obj = get_object_or_404(Telefone, id=id)
    return render(request, 'ubs/telefone/detail.html', {'obj': obj})


def update_telefone(request, id):
    obj = get_object_or_404(Telefone, id=id)
    form = TelefoneForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_telefone')
    return render(request, 'ubs/telefone/update.html', {'form': form})


