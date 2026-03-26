from django.shortcuts import render, redirect, get_object_or_404
from ..models import Hypothesis, Appointment
from ..forms import HypothesisForm


def create_hypothesis(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    form = HypothesisForm(request.POST or None)
    
    if form.is_valid():
        obj = form.save(commit=False)
        obj.appointment = appointment
        obj.save()
        return redirect('detail_appointment', id=appointment.id)

    return render(request, 'ubs/hypothesis/create.html', {'form': form})


def delete_hypothesis(request, id):
    obj = get_object_or_404(Hypothesis, id=id)
    appointment_id = obj.appointment.id
    
    obj.delete()
    
    return redirect('detail_appointment', id=appointment_id)