from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home,name="home"),
    # path('login/',views.login,name="login"),
    # path('endereco/<int:id>', views.endereco,name="endereco"),
     
     

    # ================= PESSOA =================
    path('pessoas/', views.list_pessoa, name='list_pessoa'),
    path('pessoas/novo/', views.create_pessoa, name='create_pessoa'),
    path('pessoas/<int:id>/', views.detail_pessoa, name='detail_pessoa'),
    path('pessoas/<int:id>/editar/', views.update_pessoa, name='update_pessoa'),
    path('pessoas/<int:id>/deletar/', views.delete_pessoa, name='delete_pessoa'),

    # ================= TELEFONE =================
    path('telefones/', views.list_telefone, name='list_telefone'),
    path('telefones/novo/', views.create_telefone, name='create_telefone'),
    path('telefones/<int:id>/', views.detail_telefone, name='detail_telefone'),
    path('telefones/<int:id>/editar/', views.update_telefone, name='update_telefone'),
    path('telefones/<int:id>/deletar/', views.delete_telefone, name='delete_telefone'),

    # ================= UBS =================
    path('ubs/', views.list_ubs, name='list_ubs'),
    path('ubs/novo/', views.create_ubs, name='create_ubs'),
    path('ubs/<int:id>/', views.detail_ubs, name='detail_ubs'),
    path('ubs/<int:id>/editar/', views.update_ubs, name='update_ubs'),
    path('ubs/<int:id>/deletar/', views.delete_ubs, name='delete_ubs'),

    # ================= MEDICO =================
    path('medicos/', views.list_medico, name='list_medico'),
    path('medicos/novo/', views.create_medico, name='create_medico'),
    path('medicos/<int:id>/', views.detail_medico, name='detail_medico'),
    path('medicos/<int:id>/editar/', views.update_medico, name='update_medico'),
    path('medicos/<int:id>/deletar/', views.delete_medico, name='delete_medico'),

    # ================= VACCINE =================
    path('vacinas/', views.list_vaccine, name='list_vaccine'),
    path('vacinas/novo/', views.create_vaccine, name='create_vaccine'),
    path('vacinas/<int:id>/', views.detail_vaccine, name='detail_vaccine'),
    path('vacinas/<int:id>/editar/', views.update_vaccine, name='update_vaccine'),
    path('vacinas/<int:id>/deletar/', views.delete_vaccine, name='delete_vaccine'),

    # ================= VACCINE UBS =================
    path('vacinas-ubs/', views.list_vaccine_ubs, name='list_vaccine_ubs'),
    path('vacinas-ubs/novo/', views.create_vaccine_ubs, name='create_vaccine_ubs'),
    path('vacinas-ubs/<int:id>/', views.detail_vaccine_ubs, name='detail_vaccine_ubs'),
    path('vacinas-ubs/<int:id>/editar/', views.update_vaccine_ubs, name='update_vaccine_ubs'),
    path('vacinas-ubs/<int:id>/deletar/', views.delete_vaccine_ubs, name='delete_vaccine_ubs'),

    # ================= RECORD VACCINE =================
    path('vacinas-registro/<str:num_sus>/', views.list_vaccine_records, name='list_vaccine_records'),
    path('vacinas-registro/<str:num_sus>/novo/', views.create_record_vaccine, name='create_record_vaccine'),

    # ================= EMAIL =================
    path('emails/', views.list_email, name='list_email'),
    path('emails/novo/', views.create_email, name='create_email'),
    path('emails/<int:id>/', views.detail_email, name='detail_email'),
    path('emails/<int:id>/editar/', views.update_email, name='update_email'),
    path('emails/<int:id>/deletar/', views.delete_email, name='delete_email'),

    # ================= ENFERMEIRO =================
    path('enfermeiros/', views.list_enfermeiro, name='list_enfermeiro'),
    path('enfermeiros/novo/', views.create_enfermeiro, name='create_enfermeiro'),
    path('enfermeiros/<int:id>/', views.detail_enfermeiro, name='detail_enfermeiro'),
    path('enfermeiros/<int:id>/editar/', views.update_enfermeiro, name='update_enfermeiro'),
    path('enfermeiros/<int:id>/deletar/', views.delete_enfermeiro, name='delete_enfermeiro'),

    # ================= EXAM =================
    path('exames/', views.list_exam, name='list_exam'),
    path('exames/novo/', views.create_exam, name='create_exam'),
    path('exames/<int:id>/', views.detail_exam, name='detail_exam'),
    path('exames/<int:id>/editar/', views.update_exam, name='update_exam'),
    path('exames/<int:id>/deletar/', views.delete_exam, name='delete_exam'),

    # ================= FILA =================
    path('filas/', views.list_fila, name='list_fila'),
    path('filas/novo/', views.create_fila, name='create_fila'),
    path('filas/<int:id>/', views.detail_fila, name='detail_fila'),
    path('filas/<int:id>/editar/', views.update_fila, name='update_fila'),
    path('filas/<int:id>/deletar/', views.delete_fila, name='delete_fila'),

    # ================= GRUPO =================
    path('grupos/', views.list_grupo, name='list_grupo'),
    path('grupos/novo/', views.create_grupo, name='create_grupo'),
    path('grupos/<int:id>/', views.detail_grupo, name='detail_grupo'),
    path('grupos/<int:id>/editar/', views.update_grupo, name='update_grupo'),
    path('grupos/<int:id>/deletar/', views.delete_grupo, name='delete_grupo'),

    # ================= MEDICATION =================
    path('medicamentos/', views.list_medication, name='list_medication'),
    path('medicamentos/novo/', views.create_medication, name='create_medication'),
    path('medicamentos/<int:id>/', views.detail_medication, name='detail_medication'),
    path('medicamentos/<int:id>/editar/', views.update_medication, name='update_medication'),
    path('medicamentos/<int:id>/deletar/', views.delete_medication, name='delete_medication'),

    # ================= MEDICATION UBS =================
    path('medicamentos-ubs/', views.list_medication_ubs, name='list_medication_ubs'),
    path('medicamentos-ubs/novo/', views.create_medication_ubs, name='create_medication_ubs'),
    path('medicamentos-ubs/<int:id>/', views.detail_medication_ubs, name='detail_medication_ubs'),
    path('medicamentos-ubs/<int:id>/editar/', views.update_medication_ubs, name='update_medication_ubs'),
    path('medicamentos-ubs/<int:id>/deletar/', views.delete_medication_ubs, name='delete_medication_ubs'),

    # ================= APPOINTMENT =================
    path('consultas/', views.list_appointment, name='list_appointment'),
    path('consultas/novo/', views.create_appointment, name='create_appointment'),
    path('consultas/<int:id>/', views.detail_appointment, name='detail_appointment'),
    path('consultas/<int:id>/editar/', views.update_appointment, name='update_appointment'),
    path('consultas/<int:id>/deletar/', views.delete_appointment, name='delete_appointment'),

    # ================= HYPOTHESIS =================
    path('hipoteses/<int:appointment_id>/novo/', views.create_hypothesis, name='create_hypothesis'),
    path('hipoteses/<int:id>/deletar/', views.delete_hypothesis, name='delete_hypothesis'),

    # ================= MEDICATION APPOINTMENT =================
    path('prescricoes/<int:appointment_id>/novo/', views.create_medication_appoi, name='create_medication_appoi'),
    path('prescricoes/<int:id>/deletar/', views.delete_medication_appoi, name='delete_medication_appoi'),

    # ================= CIDADAO =================
    path('cidadaos/', views.list_cidadao, name='list_cidadao'),
    path('cidadaos/novo/', views.create_cidadao, name='create_cidadao'),
    path('cidadaos/<int:id>/', views.detail_cidadao, name='detail_cidadao'),
    path('cidadaos/<int:id>/editar/', views.update_cidadao, name='update_cidadao'),
    path('cidadaos/<int:id>/deletar/', views.delete_cidadao, name='delete_cidadao'),

    # ================= DEPENDENTE =================
    path('dependentes/', views.list_dependente, name='list_dependente'),
    path('dependentes/novo/', views.create_dependente, name='create_dependente'),
    path('dependentes/<int:id>/', views.detail_dependente, name='detail_dependente'),
    path('dependentes/<int:id>/editar/', views.update_dependente, name='update_dependente'),
    path('dependentes/<int:id>/deletar/', views.delete_dependente, name='delete_dependente'),

    # ================= DOCUMENTO =================
    path('documentos/', views.list_documento, name='list_documento'),
    path('documentos/novo/', views.create_documento, name='create_documento'),
    path('documentos/<int:id>/', views.detail_documento, name='detail_documento'),
    path('documentos/<int:id>/editar/', views.update_documento, name='update_documento'),
    path('documentos/<int:id>/deletar/', views.delete_documento, name='delete_documento'),

    # ================= ADDRESS =================
    path('enderecos/', views.list_address, name='list_address'),
    path('enderecos/novo/', views.create_address, name='create_address'),
    path('enderecos/<int:id>/editar/', views.update_address, name='update_address'),
    path('enderecos/<int:id>/deletar/', views.delete_address, name='delete_address'),

    # ================= AGENDAMENTO =================
    path('agendamentos/', views.list_agendamento, name='list_agendamento'),
    path('agendamentos/novo/', views.create_agendamento, name='create_agendamento'),
    path('agendamentos/<int:id>/editar/', views.update_agendamento, name='update_agendamento'),
    path('agendamentos/<int:id>/deletar/', views.delete_agendamento, name='delete_agendamento'),

    # ================= ANAMNESE =================
    path('anamneses/', views.list_anamnese, name='list_anamnese'),
    path('anamneses/novo/', views.create_anamnese, name='create_anamnese'),
    path('anamneses/<int:id>/editar/', views.update_anamnese, name='update_anamnese'),
    path('anamneses/<int:id>/deletar/', views.delete_anamnese, name='delete_anamnese'),

]