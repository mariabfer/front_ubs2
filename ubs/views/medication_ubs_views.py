from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medication_ubs
from ..forms import MedicationUbsForm


def create_medication_ubs(request):
    form = MedicationUbsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_medication_ubs')
    return render(request, 'medication_ubs/create.html', {'form': form})


def list_medication_ubs(request):
    data = Medication_ubs.objects.select_related('medication', 'ubs').all()
    return render(request, 'medication_ubs/list.html', {'items': data})


def detail_medication_ubs(request, id):
    obj = get_object_or_404(Medication_ubs, id=id)
    return render(request, 'medication_ubs/detail.html', {'obj': obj})


def update_medication_ubs(request, id):
    obj = get_object_or_404(Medication_ubs, id=id)
    form = MedicationUbsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_medication_ubs')
    return render(request, 'medication_ubs/update.html', {'form': form})


def delete_medication_ubs(request, id):
    obj = get_object_or_404(Medication_ubs, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_medication_ubs')
    return render(request, 'medication_ubs/delete.html', {'obj': obj})