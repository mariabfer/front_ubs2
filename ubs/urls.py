from django.urls import path
from .views import address_views , pessoa_views, telefone_views, ubs_views, medico_views, vaccine_views, vaccine_ubs_views, record_vaccine_views, email_views, enfermeiro_views, exam_views, fila_atendimento_views, grupo_vulneravel_views, medication_views, medication_ubs_views, appointment_views, hypothesis_views, medication_appoi_views, cidadao_views, dependente_views, documento_views, agendamento_views, anamnese_views  

urlpatterns = [
    path('pessoas/', pessoa_views.list_pessoa, name='list_pessoa'),
    path('pessoas/novo/', pessoa_views.create_pessoa, name='create_pessoa'),
    path('pessoas/<int:id>/', pessoa_views.detail_pessoa, name='detail_pessoa'),
    path('pessoas/<int:id>/editar/', pessoa_views.update_pessoa, name='update_pessoa'),
    path('pessoas/<int:id>/deletar/', pessoa_views.delete_pessoa, name='delete_pessoa'),

    # ================= TELEFONE =================
    path('telefones/', telefone_views.list_telefone, name='list_telefone'),
    path('telefones/novo/', telefone_views.create_telefone, name='create_telefone'),
    path('telefones/<int:id>/', telefone_views.detail_telefone, name='detail_telefone'),
    path('telefones/<int:id>/editar/', telefone_views.update_telefone, name='update_telefone'),
    path('telefones/<int:id>/deletar/', telefone_views.delete_telefone, name='delete_telefone'),

    # ================= UBS =================
    path('ubs/', ubs_views.list_ubs, name='list_ubs'),
    path('ubs/novo/', ubs_views.create_ubs, name='create_ubs'),
    path('ubs/<int:id>/', ubs_views.detail_ubs, name='detail_ubs'),
    path('ubs/<int:id>/editar/', ubs_views.update_ubs, name='update_ubs'),
    path('ubs/<int:id>/deletar/', ubs_views.delete_ubs, name='delete_ubs'),

    # ================= MEDICO =================
    path('medicos/', medico_views.list_medico, name='list_medico'),
    path('medicos/novo/', medico_views.create_medico, name='create_medico'),
    path('medicos/<int:id>/', medico_views.detail_medico, name='detail_medico'),
    path('medicos/<int:id>/editar/', medico_views.update_medico, name='update_medico'),
    path('medicos/<int:id>/deletar/', medico_views.delete_medico, name='delete_medico'),

    # ================= VACCINE =================
    path('vacinas/', vaccine_views.list_vaccine, name='list_vaccine'),
    path('vacinas/novo/', vaccine_views.create_vaccine, name='create_vaccine'),
    path('vacinas/<int:id>/', vaccine_views.detail_vaccine, name='detail_vaccine'),
    path('vacinas/<int:id>/editar/', vaccine_views.update_vaccine, name='update_vaccine'),
    path('vacinas/<int:id>/deletar/', vaccine_views.delete_vaccine, name='delete_vaccine'),

    # ================= VACCINE UBS =================
    path('vacinas-ubs/', vaccine_ubs_views.list_vaccine_ubs, name='list_vaccine_ubs'),
    path('vacinas-ubs/novo/', vaccine_ubs_views.create_vaccine_ubs, name='create_vaccine_ubs'),
    path('vacinas-ubs/<int:id>/', vaccine_ubs_views.detail_vaccine_ubs, name='detail_vaccine_ubs'),
    path('vacinas-ubs/<int:id>/editar/', vaccine_ubs_views.update_vaccine_ubs, name='update_vaccine_ubs'),
    path('vacinas-ubs/<int:id>/deletar/', vaccine_ubs_views.delete_vaccine_ubs, name='delete_vaccine_ubs'),

    # ================= RECORD VACCINE =================
    path('vacinas-registro/<str:num_sus>/', record_vaccine_views.list_vaccine_records, name='list_vaccine_records'),
    path('vacinas-registro/<str:num_sus>/novo/', record_vaccine_views.create_record_vaccine, name='create_record_vaccine'),

    # ================= EMAIL =================
    path('emails/', email_views.list_email, name='list_email'),
    path('emails/novo/', email_views.create_email, name='create_email'),
    path('emails/<int:id>/', email_views.detail_email, name='detail_email'),
    path('emails/<int:id>/editar/', email_views.update_email, name='update_email'),
    path('emails/<int:id>/deletar/', email_views.delete_email, name='delete_email'),

    # ================= ENFERMEIRO =================
    path('enfermeiros/', enfermeiro_views.list_enfermeiro, name='list_enfermeiro'),
    path('enfermeiros/novo/', enfermeiro_views.create_enfermeiro, name='create_enfermeiro'),
    path('enfermeiros/<int:id>/', enfermeiro_views.detail_enfermeiro, name='detail_enfermeiro'),
    path('enfermeiros/<int:id>/editar/', enfermeiro_views.update_enfermeiro, name='update_enfermeiro'),
    path('enfermeiros/<int:id>/deletar/', enfermeiro_views.delete_enfermeiro, name='delete_enfermeiro'),

    # ================= EXAM =================
    path('exames/', exam_views.list_exam, name='list_exam'),
    path('exames/novo/', exam_views.create_exam, name='create_exam'),
    path('exames/<int:id>/', exam_views.detail_exam, name='detail_exam'),
    path('exames/<int:id>/editar/', exam_views.update_exam, name='update_exam'),
    path('exames/<int:id>/deletar/', exam_views.delete_exam, name='delete_exam'),

    # ================= FILA =================
    path('filas/', fila_atendimento_views.list_fila, name='list_fila'),
    path('filas/novo/', fila_atendimento_views.create_fila, name='create_fila'),
    path('filas/<int:id>/', fila_atendimento_views.detail_fila, name='detail_fila'),
    path('filas/<int:id>/editar/', fila_atendimento_views.update_fila, name='update_fila'),
    path('filas/<int:id>/deletar/', fila_atendimento_views.delete_fila, name='delete_fila'),

    # ================= GRUPO =================
    path('grupos/', grupo_vulneravel_views.list_grupo, name='list_grupo'),
    path('grupos/novo/', grupo_vulneravel_views.create_grupo, name='create_grupo'),
    path('grupos/<int:id>/', grupo_vulneravel_views.detail_grupo, name='detail_grupo'),
    path('grupos/<int:id>/editar/', grupo_vulneravel_views.update_grupo, name='update_grupo'),
    path('grupos/<int:id>/deletar/', grupo_vulneravel_views.delete_grupo, name='delete_grupo'),

    # ================= MEDICATION =================
    path('medicamentos/', medication_views.list_medication, name='list_medication'),
    path('medicamentos/novo/', medication_views.create_medication, name='create_medication'),
    path('medicamentos/<int:id>/', medication_views.detail_medication, name='detail_medication'),
    path('medicamentos/<int:id>/editar/', medication_views.update_medication, name='update_medication'),
    path('medicamentos/<int:id>/deletar/', medication_views.delete_medication, name='delete_medication'),

    # ================= MEDICATION UBS =================
    path('medicamentos-ubs/', medication_ubs_views.list_medication_ubs, name='list_medication_ubs'),
    path('medicamentos-ubs/novo/', medication_ubs_views.create_medication_ubs, name='create_medication_ubs'),
    path('medicamentos-ubs/<int:id>/', medication_ubs_views.detail_medication_ubs, name='detail_medication_ubs'),
    path('medicamentos-ubs/<int:id>/editar/', medication_ubs_views.update_medication_ubs, name='update_medication_ubs'),
    path('medicamentos-ubs/<int:id>/deletar/', medication_ubs_views.delete_medication_ubs, name='delete_medication_ubs'),

    # ================= APPOINTMENT =================
    path('consultas/', appointment_views.list_appointment, name='list_appointment'),
    path('consultas/novo/', appointment_views.create_appointment, name='create_appointment'),
    path('consultas/<int:id>/', appointment_views.detail_appointment, name='detail_appointment'),
    path('consultas/<int:id>/editar/', appointment_views.update_appointment, name='update_appointment'),
    path('consultas/<int:id>/deletar/', appointment_views.delete_appointment, name='delete_appointment'),

    # ================= HYPOTHESIS =================
    path('hipoteses/<int:appointment_id>/novo/', hypothesis_views.create_hypothesis, name='create_hypothesis'),
    path('hipoteses/<int:id>/deletar/', hypothesis_views.delete_hypothesis, name='delete_hypothesis'),

    # ================= MEDICATION APPOINTMENT =================
    path('prescricoes/<int:appointment_id>/novo/', medication_appoi_views.create_medication_appoi, name='create_medication_appoi'),
    path('prescricoes/<int:id>/deletar/', medication_appoi_views.delete_medication_appoi, name='delete_medication_appoi'),

    # ================= CIDADAO =================
    path('cidadaos/', cidadao_views.list_cidadao, name='list_cidadao'),
    path('cidadaos/novo/', cidadao_views.create_cidadao, name='create_cidadao'),
    path('cidadaos/<int:id>/', cidadao_views.detail_cidadao, name='detail_cidadao'),
    path('cidadaos/<int:id>/editar/', cidadao_views.update_cidadao, name='update_cidadao'),
    path('cidadaos/<int:id>/deletar/', cidadao_views.delete_cidadao, name='delete_cidadao'),

    # ================= DEPENDENTE =================
    path('dependentes/', dependente_views.list_dependente, name='list_dependente'),
    path('dependentes/novo/', dependente_views.create_dependente, name='create_dependente'),
    path('dependentes/<int:id>/', dependente_views.detail_dependente, name='detail_dependente'),
    path('dependentes/<int:id>/editar/', dependente_views.update_dependente, name='update_dependente'),
    path('dependentes/<int:id>/deletar/', dependente_views.delete_dependente, name='delete_dependente'),

    # ================= DOCUMENTO =================
    path('documentos/', documento_views.list_documento, name='list_documento'),
    path('documentos/novo/', documento_views.create_documento, name='create_documento'),
    path('documentos/<int:id>/', documento_views.detail_documento, name='detail_documento'),
    path('documentos/<int:id>/editar/', documento_views.update_documento, name='update_documento'),
    path('documentos/<int:id>/deletar/', documento_views.delete_documento, name='delete_documento'),

    # ================= ADDRESS =================
    path('enderecos/', address_views.list_address, name='list_address'),
    path('enderecos/novo/', address_views.create_address, name='create_address'),
    path('enderecos/<int:id>/editar/', address_views.update_address, name='update_address'),
    path('enderecos/<int:id>/deletar/', address_views.delete_address, name='delete_address'),

    # ================= AGENDAMENTO =================
    path('agendamentos/', agendamento_views.list_agendamento, name='list_agendamento'),
    path('agendamentos/novo/', agendamento_views.create_agendamento, name='create_agendamento'),
    path('agendamentos/<int:id>/editar/', agendamento_views.update_agendamento, name='update_agendamento'),
    path('agendamentos/<int:id>/deletar/', agendamento_views.delete_agendamento, name='delete_agendamento'),

    # ================= ANAMNESE =================
    path('anamneses/', anamnese_views.list_anamnese, name='list_anamnese'),
    path('anamneses/novo/', anamnese_views.create_anamnese, name='create_anamnese'),
    path('anamneses/<int:id>/editar/', anamnese_views.update_anamnese, name='update_anamnese'),
    path('anamneses/<int:id>/deletar/', anamnese_views.delete_anamnese, name='delete_anamnese'),

]