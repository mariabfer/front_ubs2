from django.shortcuts import render, redirect, get_object_or_404
from ..models import Ubs
from ..forms import UbsForm


def create_ubs(request):
    form = UbsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_ubs')
    return render(request, 'ubs/create.html', {'form': form})


def list_ubs(request):
    data = Ubs.objects.select_related('address').all()
    return render(request, 'ubs/list.html', {'ubs_list': data})


def detail_ubs(request, id):
    obj = get_object_or_404(Ubs, id=id)
    return render(request, 'ubs/detail.html', {'obj': obj})


def update_ubs(request, id):
    obj = get_object_or_404(Ubs, id=id)
    form = UbsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_ubs')
    return render(request, 'ubs/update.html', {'form': form})


def delete_ubs(request, id):
    obj = get_object_or_404(Ubs, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_ubs')
    return render(request, 'ubs/delete.html', {'obj': obj})