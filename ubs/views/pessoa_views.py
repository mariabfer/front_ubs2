from django.shortcuts import render, redirect, get_object_or_404
from ..models import Pessoa
from ..forms import PessoaForm


def create_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_pessoa')
    return render(request, 'pessoa/create.html', {'form': form})


def list_pessoa(request):
    data = Pessoa.objects.select_related('ubs').all()
    return render(request, 'pessoa/list.html', {'pessoas': data})


def detail_pessoa(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    return render(request, 'pessoa/detail.html', {'obj': obj})


def update_pessoa(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    form = PessoaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_pessoa')
    return render(request, 'pessoa/update.html', {'form': form})


def delete_pessoa(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_pessoa')
    return render(request, 'pessoa/delete.html', {'obj': obj})