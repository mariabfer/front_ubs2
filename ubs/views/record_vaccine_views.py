from django.shortcuts import render, redirect, get_object_or_404
from ..models import RecordVaccine, Cidadao, VaccineUbs 
from ..forms import RecordVaccineForm


def create_record_vaccine(request, num_sus):
    cidadao = get_object_or_404(Cidadao, num_sus=num_sus)

    form = RecordVaccineForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.citizen = cidadao
        obj.save()
        return redirect('detail_cidadao', id=cidadao.id)

    return render(request, 'ubs/vaccine_record/create.html', {'form': form})

def list_vaccine_records(request, num_sus):
    records = RecordVaccine.objects.select_related(
        'citizen', 'VaccineUbs ', 'nurse', 'ubs'
    ).filter(citizen__num_sus=num_sus)

    return render(request, 'ubs/vaccine_record/list.html', {
        'records': records
    })