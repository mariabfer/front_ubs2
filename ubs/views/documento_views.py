from django.shortcuts import render, redirect, get_object_or_404
from ..models import Documento
from ..forms import DocumentoForm


def create_documento(request):
    form = DocumentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_documento')
    return render(request, 'ubs/documento/create.html', {'form': form})


def list_documento(request):
    data = Documento.objects.select_related('pessoa').all()
    return render(request, 'ubs/documento/list.html', {'documentos': data})


def detail_documento(request, id):
    documento = get_object_or_404(Documento, id=id)
    return render(request, 'ubs/documento/detail.html', {'documento': documento})


def update_documento(request, id):
    obj = get_object_or_404(Documento, id=id)
    form = DocumentoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_documento')
    return render(request, 'ubs/documento/update.html', {'form': form})


