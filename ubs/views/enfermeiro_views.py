from django.shortcuts import render, redirect, get_object_or_404
from ..models import Enfermeiro
from ..forms import EnfermeiroForm


def create_enfermeiro(request):
    form = EnfermeiroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_enfermeiro')
    return render(request, 'ubs/enfermeiro/create.html', {'form': form})


def list_enfermeiro(request):
    enfermeiros = Enfermeiro.objects.select_related( 'ubs').all()
    return render(request, 'ubs/enfermeiro/list.html', {'enfermeiros': enfermeiros})


def detail_enfermeiro(request, id):
    enfermeiro = get_object_or_404(Enfermeiro, id=id)
    return render(request, 'ubs/enfermeiro/detail.html', {'enfermeiro': enfermeiro})


def update_enfermeiro(request, id):
    obj = get_object_or_404(Enfermeiro, id=id)
    form = EnfermeiroForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_enfermeiro')
    return render(request, 'ubs/enfermeiro/update.html', {'form': form})

