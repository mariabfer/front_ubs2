from django.shortcuts import render, redirect, get_object_or_404
from ..models import VaccineUbs 
from ..forms import VaccineUbsForm


def create_vaccine_ubs(request):
    form = VaccineUbsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_vaccine_ubs')
    return render(request, 'ubs/vaccine_ubs/create.html', {'form': form})


def list_vaccine_ubs(request):
    data = VaccineUbs .objects.select_related('vaccine', 'ubs').all()
    return render(request, 'ubs/vaccine_ubs/list.html', {'items': data})


def detail_vaccine_ubs(request, id):
    obj = get_object_or_404(VaccineUbs, id=id)
    return render(request, 'ubs/vaccine_ubs/detail.html', {'obj': obj})


def update_vaccine_ubs(request, id):
    obj = get_object_or_404(VaccineUbs, id=id)
    form = VaccineUbsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_vaccine_ubs')
    return render(request, 'ubs/vaccine_ubs/update.html', {'form': form})


def delete_vaccine_ubs(request, id):
    obj = get_object_or_404(VaccineUbs, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_vaccine_ubs')
    return render(request, 'ubs/vaccine_ubs/delete.html', {'obj': obj})