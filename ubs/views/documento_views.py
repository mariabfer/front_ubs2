from django.shortcuts import render, redirect, get_object_or_404
from ..models import Documento
from ..forms import DocumentoForm


def create_documento(request):
    form = DocumentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_documento')
    return render(request, 'documento/create.html', {'form': form})


def list_documento(request):
    data = Documento.objects.select_related('pessoa').all()
    return render(request, 'documento/list.html', {'documentos': data})


def detail_documento(request, id):
    obj = get_object_or_404(Documento, id=id)
    return render(request, 'documento/detail.html', {'obj': obj})


def update_documento(request, id):
    obj = get_object_or_404(Documento, id=id)
    form = DocumentoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_documento')
    return render(request, 'documento/update.html', {'form': form})


def delete_documento(request, id):
    obj = get_object_or_404(Documento, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_documento')
    return render(request, 'documento/delete.html', {'obj': obj})