from django.shortcuts import render, redirect, get_object_or_404
from ..models import Exam
from ..forms import ExamForm


def create_exam(request):
    form = ExamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_exam')
    return render(request, 'ubs/exam/create.html', {'form': form})


def list_exam(request):
    exams = Exam.objects.select_related('appointment').all()
    return render(request, 'ubs/exam/list.html', {'exams': exams})


def detail_exam(request, id):
    obj = get_object_or_404(Exam, id=id)
    return render(request, 'ubs/exam/detail.html', {'obj': obj})


def update_exam(request, id):
    obj = get_object_or_404(Exam, id=id)
    form = ExamForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('list_exam')
    return render(request, 'ubs/exam/update.html', {'form': form})


def delete_exam(request, id):
    obj = get_object_or_404(Exam, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list_exam')
    return render(request, 'ubs/exam/delete.html', {'obj': obj})