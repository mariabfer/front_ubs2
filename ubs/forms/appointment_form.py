from django import forms
from ..models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'scheduling',
            'doctor',
            'ubs',
            'data',
            'reason',
            'life_habits'
        ]

        labels = {
            'scheduling': 'Agendamento',
            'doctor': 'Médico',
            'ubs': 'UBS',
            'data': 'Data',
            'reason': 'Motivo',
            'life_habits': 'Hábitos de Vida'
        }