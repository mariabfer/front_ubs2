from django.shortcuts import render, redirect
from ..models import Focus_priority
from ..forms import FocusPriorityForm


def create_focus_priority(request):
    form = FocusPriorityForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_focus_priority')

    return render(request, 'focus_priority/create.html', {'form': form})


def list_focus_priority(request):
    data = Focus_priority.objects.select_related('type_vuln_group').all()
    
    return render(request, 'focus_priority/list.html', {
        'items': data
    })