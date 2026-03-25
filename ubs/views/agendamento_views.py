from django.shortcuts import render, redirect, get_object_or_404
from ..models import Agendamento
from ..forms import AgendamentoForm


def create_agendamento(request):
    form = AgendamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_agendamento')

    return render(request, 'agendamento/create.html', {'form': form})


def list_agendamento(request):
    agendamentos = Agendamento.objects.select_related('cidadao').all()
    return render(request, 'agendamento/list.html', {'agendamentos': agendamentos})


def update_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    form = AgendamentoForm(request.POST or None, instance=agendamento)

    if form.is_valid():
        form.save()
        return redirect('list_agendamento')

    return render(request, 'agendamento/update.html', {'form': form})


def delete_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    if request.method == "POST":
        agendamento.delete()
        return redirect('list_agendamento')

    return render(request, 'agendamento/delete.html', {'agendamento': agendamento})