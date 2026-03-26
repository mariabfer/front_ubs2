from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medication
from ..forms import MedicationForm


def create_medication(request):
    form = MedicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_medication')
    return render(request, 'ubs/medication/create.html', {'form': form})


def list_medication(request):
    data = Medication.objects.all()
    return render(request, 'ubs/medication/list.html', {'medications': data})


def detail_medication(request, id):
    medication = get_object_or_404(Medication, id=id)
    return render(request, 'ubs/medication/detail.html', {'medication': medication})


def update_medication(request, id):
    obj = get_object_or_404(Medication, id=id)
    form = MedicationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_medication')
    return render(request, 'ubs/medication/update.html', {'form': form})


def delete_medication(request, id):
    obj = get_object_or_404(Medication, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_medication')
    return render(request, 'ubs/medication/delete.html', {'obj': obj})