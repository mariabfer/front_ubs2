from django.shortcuts import render, redirect, get_object_or_404
from ..models import GrupoVulneravel 
from ..forms import GrupoVulneravelForm


def create_grupo(request):
    form = GrupoVulneravelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_grupo')
    return render(request, 'ubs/grupo/create.html', {'form': form})


def list_grupo(request):
    data = GrupoVulneravel .objects.all()
    return render(request, 'ubs/grupo/list.html', {'grupos': data})


def detail_grupo(request, id):
    obj = get_object_or_404(GrupoVulneravel , id=id)
    return render(request, 'ubs/grupo/detail.html', {'obj': obj})


def update_grupo(request, id):
    obj = get_object_or_404(GrupoVulneravel , id=id)
    form = GrupoVulneravelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_grupo')
    return render(request, 'ubs/grupo/update.html', {'form': form})


def delete_grupo(request, id):
    obj = get_object_or_404(GrupoVulneravel , id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_grupo')
    return render(request, 'ubs/grupo/delete.html', {'obj': obj})