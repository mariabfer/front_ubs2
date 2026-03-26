from django.shortcuts import render, redirect, get_object_or_404
from ..models import Appointment
from ..forms import AppointmentForm


def create_appointment(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_appointment')
    return render(request, 'ubs/appointment/create.html', {'form': form})


def list_appointment(request):
    data = Appointment.objects.select_related('scheduling', 'doctor', 'ubs').all()
    return render(request, 'ubs/appointment/list.html', {'appointments': data})


def detail_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, 'ubs/appointment/detail.html', {'appointment': appointment})


def update_appointment(request, id):
    obj = get_object_or_404(Appointment, id=id)
    form = AppointmentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_appointment')
    return render(request, 'ubs/appointment/update.html', {'form': form})


def delete_appointment(request, id):
    obj = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_appointment')
    return render(request, 'ubs/appointment/delete.html', {'obj': obj})