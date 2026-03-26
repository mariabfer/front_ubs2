from django.shortcuts import render, redirect, get_object_or_404
from ..models import MedicationUbs 
from ..forms import MedicationUbsForm


def create_medication_ubs(request):
    form = MedicationUbsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_medication_ubs')
    return render(request, 'ubs/medication_ubs/create.html', {'form': form})


def list_medication_ubs(request):
    data = MedicationUbs .objects.select_related('medication', 'ubs').all()
    return render(request, 'ubs/medication_ubs/list.html', {'items': data})


def detail_medication_ubs(request, id):
    obj = get_object_or_404(MedicationUbs , id=id)
    return render(request, 'ubs/medication_ubs/detail.html', {'obj': obj})


def update_medication_ubs(request, id):
    obj = get_object_or_404(MedicationUbs , id=id)
    form = MedicationUbsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_medication_ubs')
    return render(request, 'ubs/medication_ubs/update.html', {'form': form})


