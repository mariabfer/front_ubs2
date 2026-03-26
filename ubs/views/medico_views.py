from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medico
from ..forms import MedicoForm


def create_medico(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_medico')
    return render(request, 'ubs/medico/create.html', {'form': form})


def list_medico(request):
    data = Medico.objects.select_related( 'ubs').all()
    return render(request, 'ubs/medico/list.html', {'medicos': data})


def detail_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    return render(request, 'ubs/medico/detail.html', {'medico': medico})


def update_medico(request, id):
    obj = get_object_or_404(Medico, id=id)
    form = MedicoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_medico')
    return render(request, 'ubs/medico/update.html', {'form': form})


