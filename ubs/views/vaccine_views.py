from django.shortcuts import render, redirect, get_object_or_404
from ..models import Vaccine
from ..forms import VaccineForm


def create_vaccine(request):
    form = VaccineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_vaccine')
    return render(request, 'vaccine/create.html', {'form': form})


def list_vaccine(request):
    data = Vaccine.objects.all()
    return render(request, 'vaccine/list.html', {'vaccines': data})


def detail_vaccine(request, id):
    obj = get_object_or_404(Vaccine, id=id)
    return render(request, 'vaccine/detail.html', {'obj': obj})


def update_vaccine(request, id):
    obj = get_object_or_404(Vaccine, id=id)
    form = VaccineForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_vaccine')
    return render(request, 'vaccine/update.html', {'form': form})


def delete_vaccine(request, id):
    obj = get_object_or_404(Vaccine, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_vaccine')
    return render(request, 'vaccine/delete.html', {'obj': obj})