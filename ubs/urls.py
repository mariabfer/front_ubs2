from django.urls import path
from .views import (
    address_views, pessoa_views, telefone_views, ubs_views, medico_views,
    vaccine_views, vaccine_ubs_views, record_vaccine_views, email_views,
    enfermeiro_views, exam_views, fila_atendimento_views, grupo_vulneravel_views,
    medication_views, medication_ubs_views, appointment_views, hypothesis_views,
    medication_appoi_views, cidadao_views, dependente_views, documento_views,
    agendamento_views, anamnese_views, home_views
)

urlpatterns = [

    # HOME
    path('', home_views.home, name='home'),

    # ================= PESSOA =================
    path('pessoas/lista/', pessoa_views.list_pessoa, name='list_pessoa'),
    path('pessoas/novo/', pessoa_views.create_pessoa, name='create_pessoa'),
    path('pessoas/<int:id>/', pessoa_views.detail_pessoa, name='detail_pessoa'),
    path('pessoas/<int:id>/editar/', pessoa_views.update_pessoa, name='update_pessoa'),
    

    # ================= TELEFONE =================
    path('telefones/lista/', telefone_views.list_telefone, name='list_telefone'),
    path('telefones/novo/', telefone_views.create_telefone, name='create_telefone'),
    path('telefones/<int:id>/', telefone_views.detail_telefone, name='detail_telefone'),
    path('telefones/<int:id>/editar/', telefone_views.update_telefone, name='update_telefone'),
    

    # ================= UBS =================
    path('ubs/lista/', ubs_views.list_ubs, name='list_ubs'),
    path('ubs/novo/', ubs_views.create_ubs, name='create_ubs'),
    path('ubs/<int:id>/', ubs_views.detail_ubs, name='detail_ubs'),
    path('ubs/<int:id>/editar/', ubs_views.update_ubs, name='update_ubs'),
    

    # ================= MEDICO =================
    path('medicos/lista/', medico_views.list_medico, name='list_medico'),
    path('medicos/novo/', medico_views.create_medico, name='create_medico'),
    path('medicos/<int:id>/', medico_views.detail_medico, name='detail_medico'),
    path('medicos/<int:id>/editar/', medico_views.update_medico, name='update_medico'),
    

    # ================= VACINA =================
    path('vacinas/lista/', vaccine_views.list_vaccine, name='list_vaccine'),
    path('vacinas/novo/', vaccine_views.create_vaccine, name='create_vaccine'),
    path('vacinas/<int:id>/', vaccine_views.detail_vaccine, name='detail_vaccine'),
    path('vacinas/<int:id>/editar/', vaccine_views.update_vaccine, name='update_vaccine'),
    

    # ================= VACINA UBS =================
    path('vacinas-ubs/lista/', vaccine_ubs_views.list_vaccine_ubs, name='list_vaccine_ubs'),
    path('vacinas-ubs/novo/', vaccine_ubs_views.create_vaccine_ubs, name='create_vaccine_ubs'),
    path('vacinas-ubs/<int:id>/', vaccine_ubs_views.detail_vaccine_ubs, name='detail_vaccine_ubs'),
    path('vacinas-ubs/<int:id>/editar/', vaccine_ubs_views.update_vaccine_ubs, name='update_vaccine_ubs'),
    

    # ================= REGISTRO VACINA =================
    path('vacinas-registro/<str:num_sus>/', record_vaccine_views.list_vaccine_records, name='list_vaccine_records'),
    path('vacinas-registro/<str:num_sus>/novo/', record_vaccine_views.create_record_vaccine, name='create_record_vaccine'),

    # ================= EMAIL =================
    path('emails/lista/', email_views.list_email, name='list_email'),
    path('emails/novo/', email_views.create_email, name='create_email'),
    path('emails/<int:id>/', email_views.detail_email, name='detail_email'),
    path('emails/<int:id>/editar/', email_views.update_email, name='update_email'),


    # ================= ENFERMEIRO =================
    path('enfermeiros/lista/', enfermeiro_views.list_enfermeiro, name='list_enfermeiro'),
    path('enfermeiros/novo/', enfermeiro_views.create_enfermeiro, name='create_enfermeiro'),
    path('enfermeiros/<int:id>/', enfermeiro_views.detail_enfermeiro, name='detail_enfermeiro'),
    path('enfermeiros/<int:id>/editar/', enfermeiro_views.update_enfermeiro, name='update_enfermeiro'),
 

    # ================= EXAME =================
    path('exames/lista/', exam_views.list_exam, name='list_exam'),
    path('exames/novo/', exam_views.create_exam, name='create_exam'),
    path('exames/<int:id>/', exam_views.detail_exam, name='detail_exam'),
    path('exames/<int:id>/editar/', exam_views.update_exam, name='update_exam'),
 

    # ================= FILA =================
    path('filas/lista/', fila_atendimento_views.list_fila, name='list_fila'),
    path('filas/novo/', fila_atendimento_views.create_fila, name='create_fila'),
    path('filas/<int:id>/', fila_atendimento_views.detail_fila, name='detail_fila'),
    path('filas/<int:id>/editar/', fila_atendimento_views.update_fila, name='update_fila'),
 

    # ================= GRUPO =================
    path('grupos/lista/', grupo_vulneravel_views.list_grupo, name='list_grupo'),
    path('grupos/novo/', grupo_vulneravel_views.create_grupo, name='create_grupo'),
    path('grupos/<int:id>/', grupo_vulneravel_views.detail_grupo, name='detail_grupo'),
    path('grupos/<int:id>/editar/', grupo_vulneravel_views.update_grupo, name='update_grupo'),
  

    # ================= MEDICAMENTO =================
    path('medicamentos/lista/', medication_views.list_medication, name='list_medication'),
    path('medicamentos/novo/', medication_views.create_medication, name='create_medication'),
    path('medicamentos/<int:id>/', medication_views.detail_medication, name='detail_medication'),
    path('medicamentos/<int:id>/editar/', medication_views.update_medication, name='update_medication'),


    # ================= MEDICAMENTO UBS =================
    path('medicamentos-ubs/lista/', medication_ubs_views.list_medication_ubs, name='list_medication_ubs'),
    path('medicamentos-ubs/novo/', medication_ubs_views.create_medication_ubs, name='create_medication_ubs'),
    path('medicamentos-ubs/<int:id>/', medication_ubs_views.detail_medication_ubs, name='detail_medication_ubs'),
    path('medicamentos-ubs/<int:id>/editar/', medication_ubs_views.update_medication_ubs, name='update_medication_ubs'),
  

    # ================= CONSULTA =================
    path('consultas/lista/', appointment_views.list_appointment, name='list_appointment'),
    path('consultas/novo/', appointment_views.create_appointment, name='create_appointment'),
    path('consultas/<int:id>/', appointment_views.detail_appointment, name='detail_appointment'),
    path('consultas/<int:id>/editar/', appointment_views.update_appointment, name='update_appointment'),
   

    # ================= CIDADÃO =================
    path('cidadaos/lista/', cidadao_views.list_cidadao, name='list_cidadao'),
    path('cidadaos/novo/', cidadao_views.create_cidadao, name='create_cidadao'),
    path('cidadaos/<int:id>/', cidadao_views.detail_cidadao, name='detail_cidadao'),
    path('cidadaos/<int:id>/editar/', cidadao_views.update_cidadao, name='update_cidadao'),
  

    # ================= DEPENDENTE =================
    path('dependentes/lista/', dependente_views.list_dependente, name='list_dependente'),
    path('dependentes/novo/', dependente_views.create_dependente, name='create_dependente'),
    path('dependentes/<int:id>/', dependente_views.detail_dependente, name='detail_dependente'),
    path('dependentes/<int:id>/editar/', dependente_views.update_dependente, name='update_dependente'),
   

    # ================= DOCUMENTO =================
    path('documentos/lista/', documento_views.list_documento, name='list_documento'),
    path('documentos/novo/', documento_views.create_documento, name='create_documento'),
    path('documentos/<int:id>/', documento_views.detail_documento, name='detail_documento'),
    path('documentos/<int:id>/editar/', documento_views.update_documento, name='update_documento'),
   

    # ================= ENDEREÇO =================
    path('enderecos/lista/', address_views.list_address, name='list_address'),
    path('enderecos/novo/', address_views.create_address, name='create_address'),
    path('enderecos/<int:id>/', address_views.detail_address, name='detail_address'),
    path('enderecos/<int:id>/editar/', address_views.update_address, name='update_address'),
   

    # ================= AGENDAMENTO =================
    path('agendamentos/lista/', agendamento_views.list_agendamento, name='list_agendamento'),
    path('agendamentos/novo/', agendamento_views.create_agendamento, name='create_agendamento'),
    path('agendamentos/<int:id>/', agendamento_views.detail_agendamento, name='detail_agendamento'),
    path('agendamentos/<int:id>/editar/', agendamento_views.update_agendamento, name='update_agendamento'),
   

    # ================= ANAMNESE =================
    path('anamneses/lista/', anamnese_views.list_anamnese, name='list_anamnese'),
    path('anamneses/novo/', anamnese_views.create_anamnese, name='create_anamnese'),
    path('anamneses/<int:id>/', anamnese_views.detail_anamnese, name='detail_anamnese'),
    path('anamneses/<int:id>/editar/', anamnese_views.update_anamnese, name='update_anamnese'),
   
]