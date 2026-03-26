from django.shortcuts import render, redirect, get_object_or_404
from ..models import MedicationAppoi , Appointment
from ..forms import MedicationAppoiForm


def create_medication_appoi(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    form = MedicationAppoiForm(request.POST or None)
    
    if form.is_valid():
        obj = form.save(commit=False)
        obj.appointment = appointment
        obj.save()
        return redirect('detail_appointment', id=appointment.id)

    return render(request, 'ubs/medication_appoi/create.html', {'form': form})

def list_medication_appoi(request):
    medications = MedicationAppoi.objects.all()
    return render(request, 'ubs/medication_appoi/create/list.html', {'medications': medications})

def delete_medication_appoi(request, id):
    obj = get_object_or_404(MedicationAppoi , id=id)
    appointment_id = obj.appointment.id
    
    obj.delete()
    
    return redirect('detail_appointment', id=appointment_id)