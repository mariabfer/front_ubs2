from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medico
from ..forms import MedicoForm


def create_medico(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_medico')
    return render(request, 'medico/create.html', {'form': form})


def list_medico(request):
    data = Medico.objects.select_related('pessoa', 'ubs').all()
    return render(request, 'medico/list.html', {'medicos': data})


def detail_medico(request, id):
    obj = get_object_or_404(Medico, id=id)
    return render(request, 'medico/detail.html', {'obj': obj})


def update_medico(request, id):
    obj = get_object_or_404(Medico, id=id)
    form = MedicoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_medico')
    return render(request, 'medico/update.html', {'form': form})


def delete_medico(request, id):
    obj = get_object_or_404(Medico, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_medico')
    return render(request, 'medico/delete.html', {'obj': obj})