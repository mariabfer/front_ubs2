# ADDRESS
from .address_views import create_address, list_address, update_address

# AGENDAMENTO
from .agendamento_views import create_agendamento, list_agendamento, update_agendamento

# ANAMNESE
from .anamnese_views import create_anamnese, list_anamnese, update_anamnese

# APPOINTMENT
from .appointment_views import create_appointment, list_appointment, detail_appointment, update_appointment

# CIDADAO
from .cidadao_views import create_cidadao, list_cidadao, detail_cidadao, update_cidadao
# DEPENDENTE
from .dependente_views import create_dependente, list_dependente, detail_dependente, update_dependente

# DOCUMENTO
from .documento_views import create_documento, list_documento, detail_documento, update_documento

# EMAIL
from .email_views import create_email, list_email, detail_email, update_email

# ENFERMEIRO
from .enfermeiro_views import create_enfermeiro, list_enfermeiro, detail_enfermeiro, update_enfermeiro

# EXAM
from .exam_views import create_exam, list_exam, detail_exam, update_exam

# FILA
from .fila_atendimento_views import create_fila, list_fila, detail_fila, update_fila

# FOCUS PRIORITY
from .focus_priority_views import create_focus_priority, list_focus_priority

# GRUPO
from .grupo_vulneravel_views import create_grupo, list_grupo, detail_grupo, update_grupo

# HYPOTHESIS
from .hypothesis_views import create_hypothesis

# MEDICATION APPOINTMENT
from .medication_appoi_views import create_medication_appoi

# MEDICATION
from .medication_views import create_medication, list_medication, detail_medication, update_medication

# MEDICATION UBS
from .medication_ubs_views import create_medication_ubs, list_medication_ubs, detail_medication_ubs, update_medication_ubs

# MEDICO
from .medico_views import create_medico, list_medico, detail_medico, update_medico

# PESSOA
from .pessoa_views import create_pessoa, list_pessoa, detail_pessoa, update_pessoa

# RECORD VACCINE
from .record_vaccine_views import create_record_vaccine, list_vaccine_records

# TELEFONE
from .telefone_views import create_telefone, list_telefone, detail_telefone, update_telefone

# UBS
from .ubs_views import create_ubs, list_ubs, detail_ubs, update_ubs

# VACCINE
from .vaccine_views import create_vaccine, list_vaccine, detail_vaccine, update_vaccine

# VACCINE UBS
from .vaccine_ubs_views import create_vaccine_ubs, list_vaccine_ubs, detail_vaccine_ubs, update_vaccine_ubs