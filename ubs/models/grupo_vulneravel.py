from django.db import models


class NomeGrupo(models.TextChoices):
    RECEM_NASCIDOS = "RECEM_NASCIDOS", "Recém-nascidos"
    CRIANCA = "CRIANCA", "Crianças"
    GESTANTE = "GESTANTE", "Gestantes"
    PUERPERA = "PUERPERA", "Puérperas"
    IDOSO = "IDOSO", "Idosos"
    DOENCA_CRONICA = "DOENCA_CRONICA", "Doenças crônicas"
    DEFICIENCIA = "DEFICIENCIA", "Pessoa com deficiência"
    SAUDE_MENTAL = "SAUDE_MENTAL", "Transtornos mentais"
    SITUACAO_DE_RUA = "SITUACAO_DE_RUA", "Situação de rua"
    INDIGENA = "INDIGENA", "População indígena"
    QUILOMBOLA = "QUILOMBOLA", "População quilombola"
    PRIVADO_LIBERDADE = "PRIVADO_LIBERDADE", "Privado de liberdade"
    USUARIO_DROGAS = "USUARIO_DROGAS", "Usuários de drogas"
    HIV_IST = "HIV_IST", "HIV/IST"
    ADOLESCENTE = "ADOLESCENTE", "Adolescentes"
    VITIMA_VIOLENCIA = "VITIMA_VIOLENCIA", "Vítima de violência"


class GrupoVulneravel(models.Model):
    nome_grupo = models.CharField(
        max_length=50,
        choices=NomeGrupo.choices,
        unique=True
    )

    peso_prioridade = models.IntegerField()

    descricao = models.TextField()

    def __str__(self):
        return f"{self.get_nome_grupo_display()} (peso: {self.peso_prioridade})"