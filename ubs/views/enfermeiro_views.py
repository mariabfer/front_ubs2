from django.shortcuts import render, redirect, get_object_or_404
from ..models import Enfermeiro
from ..forms import EnfermeiroForm


def create_enfermeiro(request):
    form = EnfermeiroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_enfermeiro')
    return render(request, 'enfermeiro/create.html', {'form': form})


def list_enfermeiro(request):
    enfermeiros = Enfermeiro.objects.select_related('pessoa', 'ubs').all()
    return render(request, 'enfermeiro/list.html', {'enfermeiros': enfermeiros})


def detail_enfermeiro(request, id):
    obj = get_object_or_404(Enfermeiro, id=id)
    return render(request, 'enfermeiro/detail.html', {'obj': obj})


def update_enfermeiro(request, id):
    obj = get_object_or_404(Enfermeiro, id=id)
    form = EnfermeiroForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_enfermeiro')
    return render(request, 'enfermeiro/update.html', {'form': form})


def delete_enfermeiro(request, id):
    obj = get_object_or_404(Enfermeiro, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_enfermeiro')
    return render(request, 'enfermeiro/delete.html', {'obj': obj})