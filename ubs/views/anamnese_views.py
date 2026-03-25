from django.shortcuts import render, redirect, get_object_or_404
from ..models import Anamnese
from ..forms import AnamneseForm


def create_anamnese(request):
    form = AnamneseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_anamnese')

    return render(request, 'anamnese/create.html', {'form': form})


def list_anamnese(request):
    anamneses = Anamnese.objects.select_related('cidadao').all()
    return render(request, 'anamnese/list.html', {'anamneses': anamneses})


def update_anamnese(request, id):
    anamnese = get_object_or_404(Anamnese, id=id)
    form = AnamneseForm(request.POST or None, instance=anamnese)

    if form.is_valid():
        form.save()
        return redirect('list_anamnese')

    return render(request, 'anamnese/update.html', {'form': form})


def delete_anamnese(request, id):
    anamnese = get_object_or_404(Anamnese, id=id)

    if request.method == "POST":
        anamnese.delete()
        return redirect('list_anamnese')

    return render(request, 'anamnese/delete.html', {'anamnese': anamnese})