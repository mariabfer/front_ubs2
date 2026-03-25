from django.shortcuts import render, redirect
from ..models import FocusPriority 
from ..forms import FocusPriorityForm


def create_focus_priority(request):
    form = FocusPriorityForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_focus_priority')

    return render(request, 'focus_priority/create.html', {'form': form})


def list_focus_priority(request):
    data = FocusPriority .objects.select_related('grupo_vulneravel').all()
    
    return render(request, 'focus_priority/list.html', {
        'items': data
    })