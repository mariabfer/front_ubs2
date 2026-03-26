from django.shortcuts import render, redirect, get_object_or_404
from ..models import Email
from ..forms import EmailForm


def create_email(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_email')
    return render(request, 'ubs/email/create.html', {'form': form})


def list_email(request):
    data = Email.objects.select_related('pessoa', 'ubs').all()
    return render(request, 'ubs/email/list.html', {'emails': data})


def detail_email(request, id):
    email = get_object_or_404(Email, id=id)
    return render(request, 'ubs/email/detail.html', {'email': email})


def update_email(request, id):
    obj = get_object_or_404(Email, id=id)
    form = EmailForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_email')
    return render(request, 'ubs/email/update.html', {'form': form})

