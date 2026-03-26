from django.shortcuts import render, redirect, get_object_or_404
from ..models import Agendamento
from ..forms import AgendamentoForm


def create_agendamento(request):
    form = AgendamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_agendamento')

    return render(request, 'ubs/agendamento/create.html', {'form': form})


def list_agendamento(request):
    agendamentos = Agendamento.objects.select_related('cidadao').order_by('-prioridade_calculada')

    return render(request, 'ubs/agendamento/list.html', {
        'agendamentos': agendamentos
    })

def update_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    form = AgendamentoForm(request.POST or None, instance=agendamento)

    if form.is_valid():
        form.save()
        return redirect('list_agendamento')

    return render(request, 'ubs/agendamento/update.html', {'form': form})


def detail_agendamento(request, id):
    agendamentos = get_object_or_404(Agendamento, id=id)
    return render(request, 'ubs/agendamento/detail.html', {'agendamento': agendamentos})