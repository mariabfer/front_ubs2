# from ubs.models import Address

# def seed_address():

#     Address.objects.bulk_create([
#         Address(cep="63180000", state="CE", city="Barbalha", neigh="Centro", street="Rua das Flores", number="12"),
#         Address(cep="63010120", state="CE", city="Juazeiro do Norte", neigh="Centro", street="Rua José Marrocos", number="15"),
#         Address(cep="63050300", state="CE", city="Juazeiro do Norte", neigh="Romeirão", street="Rua Santa Luzia", number="33"),
#         Address(cep="63105000", state="CE", city="Crato", neigh="Pimenta", street="Rua Coronel Teixeira", number="886"),
#         Address(cep="63041000", state="CE", city="Juazeiro do Norte", neigh="Triângulo", street="Rua São Francisco", number="543"),
#         Address(cep="63010050", state="CE", city="Juazeiro do Norte", neigh="Centro", street="Rua das Acácias", number="45"),
#         Address(cep="63050210", state="CE", city="Juazeiro do Norte", neigh="Centro", street="Rua Padre Cícero", number="120"),
#         Address(cep="63041020", state="CE", city="Juazeiro do Norte", neigh="Triângulo", street="Rua São Pedro", number="78"),
#         Address(cep="63050560", state="CE", city="Barbalha", neigh="Bairro do Rosário", street="Rua Bela Vista", number="210"),
#         Address(cep="63180020", state="CE", city="Barbalha", neigh="Centro", street="Rua da Paz", number="33"),
#         Address(cep="63106030", state="CE", city="Crato", neigh="Muriti", street="Rua Nova Esperança", number="92"),
#         Address(cep="63100040", state="CE", city="Crato", neigh="Centro", street="Rua José de Alencar", number="150"),
#         Address(cep="63105070", state="CE", city="Crato", neigh="Pimenta", street="Rua Dom Pedro II", number="64"),
#         Address(cep="63180040", state="CE", city="Barbalha", neigh="Centro", street="Rua São José", number="81"),
#         Address(cep="63041230", state="CE", city="Juazeiro do Norte", neigh="Triângulo", street="Rua das Mangueiras", number="305"),
#         Address(cep="63180000", state="CE", city="Barbalha", neigh="Centro", street="Rua Santo Antônio", number="45"),
#         Address(cep="63180020", state="CE", city="Barbalha", neigh="Malvinas", street="Rua Padre Ibiapina", number="120"),
#         Address(cep="63050000", state="CE", city="Juazeiro do Norte", neigh="Romeirão", street="Rua São Jorge", number="101"),
#         Address(cep="63050010", state="CE", city="Juazeiro do Norte", neigh="Romeirão", street="Rua das Oliveiras", number="202"),
#         Address(cep="63050020", state="CE", city="Juazeiro do Norte", neigh="Romeirão", street="Rua Padre Cícero", number="303"),
#         Address(cep="63050030", state="CE", city="Juazeiro do Norte", neigh="Romeirão", street="Rua Santa Luzia", number="404"),
#         Address(cep="63050040", state="CE", city="Juazeiro do Norte", neigh="Romeirão", street="Rua do Rosário", number="505"),
#         Address(cep="63010000", state="CE", city="Juazeiro do Norte", neigh="Centro", street="Rua São Pedro", number="88"),
#         Address(cep="63010020", state="CE", city="Juazeiro do Norte", neigh="Centro", street="Rua São Paulo", number="190"),
#         Address(cep="63041000", state="CE", city="Juazeiro do Norte", neigh="Triângulo", street="Rua das Mangueiras", number="50"),
#         Address(cep="63041010", state="CE", city="Juazeiro do Norte", neigh="Triângulo", street="Rua das Palmeiras", number="61"),
#         Address(cep="63041020", state="CE", city="Juazeiro do Norte", neigh="Triângulo", street="Rua José de Alencar", number="72"),
#         Address(cep="63041030", state="CE", city="Juazeiro do Norte", neigh="Triângulo", street="Rua Padre Cícero", number="83"),
#         Address(cep="63100000", state="CE", city="Crato", neigh="Centro", street="Rua Coronel Antônio Luiz", number="150"),
#         Address(cep="63105000", state="CE", city="Crato", neigh="Pimenta", street="Rua Tristão Gonçalves", number="320"),
#     ])

#     print("ENDEREÇOS INSERIDOS")


from ubs.models import Vaccine

def seed_vaccine():

    Vaccine.objects.bulk_create([
        Vaccine(type_vaccine="BCG", vaccine_manufacturer="SUS", prevents="Formas graves da tuberculose"),
        Vaccine(type_vaccine="Hepatite B", vaccine_manufacturer="SUS", prevents="Infecção crônica do fígado causada pelo vírus da hepatite B"),
        Vaccine(type_vaccine="Pentavalente (DTP/Hib/Hep B)", vaccine_manufacturer="SUS", prevents="Difteria, tétano, coqueluche, meningite e outras infecções"),
        Vaccine(type_vaccine="VIP (Poliomielite inativada)", vaccine_manufacturer="SUS", prevents="Poliomielite"),
        Vaccine(type_vaccine="VOP (Poliomielite oral)", vaccine_manufacturer="SUS", prevents="Poliomielite reforço"),
        Vaccine(type_vaccine="Rotavírus Humano (VRH)", vaccine_manufacturer="SUS", prevents="Diarreia grave por rotavírus"),
        Vaccine(type_vaccine="Meningocócica C (Conjugada)", vaccine_manufacturer="SUS", prevents="Meningite tipo C"),
        Vaccine(type_vaccine="Pneumocócica 10-valente", vaccine_manufacturer="SUS", prevents="Pneumonia e meningite"),
        Vaccine(type_vaccine="Tríplice Viral (SCR)", vaccine_manufacturer="SUS", prevents="Sarampo, caxumba e rubéola"),
        Vaccine(type_vaccine="Febre Amarela", vaccine_manufacturer="SUS", prevents="Febre amarela"),
        Vaccine(type_vaccine="HPV4", vaccine_manufacturer="SUS", prevents="Câncer relacionado ao HPV"),
        Vaccine(type_vaccine="Meningocócica ACWY", vaccine_manufacturer="SUS", prevents="Meningites A, C, W e Y"),
        Vaccine(type_vaccine="dT (Dupla Adulto)", vaccine_manufacturer="SUS", prevents="Difteria e tétano"),
        Vaccine(type_vaccine="Influenza", vaccine_manufacturer="SUS", prevents="Gripe influenza"),
        Vaccine(type_vaccine="Covid-19", vaccine_manufacturer="Pfizer", prevents="COVID-19"),
        Vaccine(type_vaccine="Pneumocócica 23-valente", vaccine_manufacturer="SUS", prevents="Pneumonia grave"),
        Vaccine(type_vaccine="dTpa", vaccine_manufacturer="SUS", prevents="Difteria, tétano e coqueluche"),
    ])

    print("VACINAS INSERIDAS")

from ubs.models import GrupoVulneravel

def seed_grupo():

    GrupoVulneravel.objects.bulk_create([
        GrupoVulneravel(nome_grupo="IMUNOSSUPRIMIDOS", peso_prioridade=5, descricao="Sistema imunológico enfraquecido"),
        GrupoVulneravel(nome_grupo="CRIANCA", peso_prioridade=5, descricao="Crianças"),
        GrupoVulneravel(nome_grupo="GESTANTE", peso_prioridade=5, descricao="Gestantes"),
        GrupoVulneravel(nome_grupo="PUERPERA", peso_prioridade=4, descricao="Pós-parto"),
        GrupoVulneravel(nome_grupo="IDOSO", peso_prioridade=5, descricao="Idosos"),
        GrupoVulneravel(nome_grupo="DOENCA_CRONICA", peso_prioridade=4, descricao="Doenças crônicas"),
        GrupoVulneravel(nome_grupo="DEFICIENCIA", peso_prioridade=4, descricao="Pessoa com deficiência"),
        GrupoVulneravel(nome_grupo="SAUDE_MENTAL", peso_prioridade=3, descricao="Transtornos mentais"),
        GrupoVulneravel(nome_grupo="SITUACAO_DE_RUA", peso_prioridade=4, descricao="Situação de rua"),
        GrupoVulneravel(nome_grupo="INDIGENA", peso_prioridade=5, descricao="População indígena"),
        GrupoVulneravel(nome_grupo="QUILOMBOLA", peso_prioridade=5, descricao="População quilombola"),
        GrupoVulneravel(nome_grupo="PRIVADO_LIBERDADE", peso_prioridade=4, descricao="Privado de liberdade"),
        GrupoVulneravel(nome_grupo="USUARIO_DROGAS", peso_prioridade=3, descricao="Usuários de drogas"),
        GrupoVulneravel(nome_grupo="HIV_IST", peso_prioridade=5, descricao="HIV/IST"),
        GrupoVulneravel(nome_grupo="ADOLESCENTE", peso_prioridade=3, descricao="Adolescentes"),
        GrupoVulneravel(nome_grupo="VITIMA_VIOLENCIA", peso_prioridade=4, descricao="Vítima de violência"),
        GrupoVulneravel(nome_grupo="RECEM_NASCIDOS", peso_prioridade=5, descricao="Recém-nascidos"),
    ])

    print("GRUPOS INSERIDOS")


from ubs.models import Ubs, Address

def seed_ubs():

    enderecos = list(Address.objects.all())

    Ubs.objects.bulk_create([
        Ubs(name="UBS Romeirao", address=enderecos[2]),
        Ubs(name="UBS Barbalha", address=enderecos[9]),
        Ubs(name="UBS Centro", address=enderecos[1]),
        Ubs(name="UBS Triangulo", address=enderecos[4]),
        Ubs(name="UBS Crato", address=enderecos[12]),
    ])

    print("UBS INSERIDAS")

# from ubs.models import *

# def run():

#     ubs_list = list(Ubs.objects.all())

#     # UBS 0
#     Medico.objects.create(nome_pessoa="Carla Mendes Ferreira", estado_civil="UNIAO_ESTAVEL", ubs=ubs_list[0], crm="1001-CE", especialidade="Ginecologia")
#     Medico.objects.create(nome_pessoa="Larissa Martins Carvalho", estado_civil="CASADO", ubs=ubs_list[0], crm="1002-CE", especialidade="Pediatria")
#     Medico.objects.create(nome_pessoa="Fernanda Gomes Barbosa", estado_civil="DIVORCIADO", ubs=ubs_list[0], crm="1003-CE", especialidade="Psiquiatria")
#     Medico.objects.create(nome_pessoa="Bruna Alves Rodrigues", estado_civil="SOLTEIRO", ubs=ubs_list[0], crm="1004-CE", especialidade="Clínico Geral")

#     # UBS 1
#     Medico.objects.create(nome_pessoa="Tatiane Souza Martins", estado_civil="CASADO", ubs=ubs_list[1], crm="1005-CE", especialidade="Cardiologia")
#     Medico.objects.create(nome_pessoa="Gabriela Ribeiro Fernandes", estado_civil="SOLTEIRO", ubs=ubs_list[1], crm="1006-CE", especialidade="Dermatologia")
#     Medico.objects.create(nome_pessoa="Patrícia Alves Monteiro", estado_civil="CASADO", ubs=ubs_list[1], crm="1007-CE", especialidade="Pediatria")
#     Medico.objects.create(nome_pessoa="Debora Lima Carvalho", estado_civil="DIVORCIADO", ubs=ubs_list[1], crm="1008-CE", especialidade="Clínico Geral")

#     # UBS 2
#     Medico.objects.create(nome_pessoa="Aline Rocha Pereira", estado_civil="UNIAO_ESTAVEL", ubs=ubs_list[2], crm="1009-CE", especialidade="Ginecologia")
#     Medico.objects.create(nome_pessoa="Renata Rocha Cardoso", estado_civil="CASADO", ubs=ubs_list[2], crm="1010-CE", especialidade="Endocrinologia")
#     Medico.objects.create(nome_pessoa="Vanessa Teixeira Lopes", estado_civil="SOLTEIRO", ubs=ubs_list[2], crm="1011-CE", especialidade="Neurologia")
#     Medico.objects.create(nome_pessoa="Rodrigo Alves Ferreira", estado_civil="CASADO", ubs=ubs_list[2], crm="1012-CE", especialidade="Clínico Geral")

#     # UBS 3
#     Medico.objects.create(nome_pessoa="Patrícia Gomes Barbosa", estado_civil="DIVORCIADO", ubs=ubs_list[3], crm="1013-CE", especialidade="Ortopedia")
#     Medico.objects.create(nome_pessoa="Carlos Eduardo Mendes Silva", estado_civil="CASADO", ubs=ubs_list[3], crm="1014-CE", especialidade="Ginecologia")
#     Medico.objects.create(nome_pessoa="Fernanda Cristina Alves Rocha", estado_civil="SOLTEIRO", ubs=ubs_list[3], crm="1015-CE", especialidade="Oftalmologia")
#     Medico.objects.create(nome_pessoa="Paulo Henrique Batista Souza", estado_civil="DIVORCIADO", ubs=ubs_list[3], crm="1016-CE", especialidade="Clínico Geral")

#     # UBS 4
#     Medico.objects.create(nome_pessoa="Juliana Martins de Oliveira", estado_civil="CASADO", ubs=ubs_list[4], crm="1017-CE", especialidade="Ginecologia")
#     Medico.objects.create(nome_pessoa="Ricardo Gomes Pereira", estado_civil="SOLTEIRO", ubs=ubs_list[4], crm="1018-CE", especialidade="Pediatria")
#     Medico.objects.create(nome_pessoa="Aline Barbosa dos Santos", estado_civil="UNIAO_ESTAVEL", ubs=ubs_list[4], crm="1019-CE", especialidade="Psiquiatria")
#     Medico.objects.create(nome_pessoa="Marcos Vinicius Teixeira Lima", estado_civil="CASADO", ubs=ubs_list[4], crm="1020-CE", especialidade="Clínico Geral")


#     # UBS 0
#     Enfermeiro.objects.create(nome_pessoa="Patricia Fernandes Costa", estado_civil="SOLTEIRO", ubs=ubs_list[0], cip="ENF1001")
#     Enfermeiro.objects.create(nome_pessoa="João Victor Almeida Santos", estado_civil="SOLTEIRO", ubs=ubs_list[0], cip="ENF1002")

#     # UBS 1
#     Enfermeiro.objects.create(nome_pessoa="Beatriz Oliveira Mendes", estado_civil="CASADO", ubs=ubs_list[1], cip="ENF1003")
#     Enfermeiro.objects.create(nome_pessoa="Lucas Henrique Rocha Lima", estado_civil="SOLTEIRO", ubs=ubs_list[1], cip="ENF1004")

#     # UBS 2
#     Enfermeiro.objects.create(nome_pessoa="Amanda Cristina Barbosa Alves", estado_civil="SOLTEIRO", ubs=ubs_list[2], cip="ENF1005")
#     Enfermeiro.objects.create(nome_pessoa="Pedro Augusto Fernandes Souza", estado_civil="CASADO", ubs=ubs_list[2], cip="ENF1006")

#     # UBS 3
#     Enfermeiro.objects.create(nome_pessoa="Larissa Beatriz Costa Ribeiro", estado_civil="SOLTEIRO", ubs=ubs_list[3], cip="ENF1007")
#     Enfermeiro.objects.create(nome_pessoa="Camila Rocha Pereira", estado_civil="SOLTEIRO", ubs=ubs_list[3], cip="ENF1008")

#     # UBS 4
#     Enfermeiro.objects.create(nome_pessoa="Rafael Gomes Barbosa", estado_civil="SOLTEIRO", ubs=ubs_list[4], cip="ENF1009")
#     Enfermeiro.objects.create(nome_pessoa="Felipe Souza Martins", estado_civil="SOLTEIRO", ubs=ubs_list[4], cip="ENF1010")


from ubs.models import *

def run():

    ubs_list = list(Ubs.objects.all())
    enderecos = list(Address.objects.all())

    # =========================
    # UBS 0 (1234567)
    # =========================

    c1 = Cidadao.objects.create(nome_pessoa="Vinicius Andrade Silva", estado_civil="DIVORCIADO", num_sus="9000001", data_nascimento="1985-02-12", genero="M", naturalidade="Juazeiro do Norte", ocupacao="Pedreiro", address=enderecos[18], ubs=ubs_list[0])
    Documento.objects.create(pessoa=c1, tipo_documento="CPF", numero_documento="487.354.827-46")

    c2 = Cidadao.objects.create(nome_pessoa="Camila Renata Gomes Barbosa", estado_civil="CASADO", num_sus="9000002", data_nascimento="1990-04-21", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Professora", address=enderecos[19], ubs=ubs_list[0])
    Documento.objects.create(pessoa=c2, tipo_documento="CPF", numero_documento="593.148.276-55")

    c3 = Cidadao.objects.create(nome_pessoa="Mariana Lima Pereira", estado_civil="SOLTEIRO", num_sus="9000003", data_nascimento="2001-07-10", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Recepcionista", address=enderecos[20], ubs=ubs_list[0])
    Documento.objects.create(pessoa=c3, tipo_documento="CPF", numero_documento="712.639.845-03")

    c4 = Cidadao.objects.create(nome_pessoa="Patricia Helena Souza Martins", estado_civil="CASADO", num_sus="9000004", data_nascimento="1988-09-30", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Costureira", address=enderecos[21], ubs=ubs_list[0])
    Documento.objects.create(pessoa=c4, tipo_documento="CPF", numero_documento="864.120.593-91")

    # crianças
    c5 = Cidadao.objects.create(nome_pessoa="Lucas Andrade Silva", estado_civil="SOLTEIRO", num_sus="9500001", data_nascimento="2026-03-01", genero="M", naturalidade="Juazeiro do Norte", ocupacao="Recém-nascido", address=enderecos[18], ubs=ubs_list[0])
    Documento.objects.create(pessoa=c5, tipo_documento="CERTIDAO_NASCIMENTO", numero_documento="CN-2025-000025")

    c6 = Cidadao.objects.create(nome_pessoa="Mariana Andrade Silva", estado_civil="SOLTEIRO", num_sus="9500003", data_nascimento="2018-04-12", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Estudante", address=enderecos[18], ubs=ubs_list[0])
    Documento.objects.create(pessoa=c6, tipo_documento="CERTIDAO_NASCIMENTO", numero_documento="CN-2025-000026")

    c7 = Cidadao.objects.create(nome_pessoa="Ana Beatriz Gomes Barbosa", estado_civil="SOLTEIRO", num_sus="9500005", data_nascimento="2016-06-21", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Estudante", address=enderecos[20], ubs=ubs_list[0])
    Documento.objects.create(pessoa=c7, tipo_documento="CERTIDAO_NASCIMENTO", numero_documento="CN-2025-000029")

    # =========================
    # UBS 1 (2749826)
    # =========================

    c8 = Cidadao.objects.create(nome_pessoa="Carlos Eduardo Almeida Rocha", estado_civil="SOLTEIRO", num_sus="9000005", data_nascimento="1983-05-12", genero="M", naturalidade="Barbalha", ocupacao="Comerciante", address=enderecos[1], ubs=ubs_list[1])
    Documento.objects.create(pessoa=c8, tipo_documento="CPF", numero_documento="295.743.168-44")

    c9 = Cidadao.objects.create(nome_pessoa="Mariana Fernanda Ribeiro Costa", estado_civil="CASADO", num_sus="9000006", data_nascimento="1989-03-19", genero="F", naturalidade="Barbalha", ocupacao="Enfermeira", address=enderecos[14], ubs=ubs_list[1])
    Documento.objects.create(pessoa=c9, tipo_documento="CPF", numero_documento="348.915.702-66")

    c10 = Cidadao.objects.create(nome_pessoa="Carla Mendes Monteiro Souza", estado_civil="CASADO", num_sus="9000007", data_nascimento="1992-08-22", genero="F", naturalidade="Barbalha", ocupacao="Secretária", address=enderecos[16], ubs=ubs_list[1])
    Documento.objects.create(pessoa=c10, tipo_documento="CPF", numero_documento="629.504.813-77")

    c11 = Cidadao.objects.create(nome_pessoa="Juliana Costa Ribeiro Santos", estado_civil="CASADO", num_sus="9000008", data_nascimento="1991-10-02", genero="F", naturalidade="Barbalha", ocupacao="Vendedora", address=enderecos[29], ubs=ubs_list[1])
    Documento.objects.create(pessoa=c11, tipo_documento="CPF", numero_documento="703.281.694-20")

    # =========================
    # UBS 2 (7654321)
    # =========================

    c12 = Cidadao.objects.create(nome_pessoa="Marcos Batista Nogueira", estado_civil="CASADO", num_sus="9000009", data_nascimento="1979-11-18", genero="M", naturalidade="Juazeiro do Norte", ocupacao="Motorista", address=enderecos[6], ubs=ubs_list[2])
    Documento.objects.create(pessoa=c12, tipo_documento="CPF", numero_documento="514.837.206-18")

    c13 = Cidadao.objects.create(nome_pessoa="Patrícia Martins Cardoso", estado_civil="SOLTEIRO", num_sus="9000010", data_nascimento="1987-06-20", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Cabeleireira", address=enderecos[7], ubs=ubs_list[2])
    Documento.objects.create(pessoa=c13, tipo_documento="CPF", numero_documento="678.349.520-31")

    c14 = Cidadao.objects.create(nome_pessoa="Juliana Alves Rocha", estado_civil="SOLTEIRO", num_sus="9000011", data_nascimento="1993-02-11", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Auxiliar Administrativo", address=enderecos[23], ubs=ubs_list[2])
    Documento.objects.create(pessoa=c14, tipo_documento="CPF", numero_documento="145.983.762-04")

    c15 = Cidadao.objects.create(nome_pessoa="Carlos Eduardo Lima", estado_civil="CASADO", num_sus="9000012", data_nascimento="1986-12-01", genero="M", naturalidade="Juazeiro do Norte", ocupacao="Vendedor", address=enderecos[24], ubs=ubs_list[2])
    Documento.objects.create(pessoa=c15, tipo_documento="CPF", numero_documento="208.764.951-63")

    c16 = Cidadao.objects.create(nome_pessoa="Fernanda Costa Ribeiro", estado_civil="SOLTEIRO", num_sus="9000013", data_nascimento="1995-09-09", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Atendente", address=enderecos[6], ubs=ubs_list[2])
    Documento.objects.create(pessoa=c16, tipo_documento="CPF", numero_documento="359.820.174-55")

    # =========================
    # UBS 3 (8765432)
    # =========================

    c17 = Cidadao.objects.create(nome_pessoa="Camila Gomes Silva", estado_civil="SOLTEIRO", num_sus="9000014", data_nascimento="1990-01-30", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Operadora de Caixa", address=enderecos[8], ubs=ubs_list[3])
    Documento.objects.create(pessoa=c17, tipo_documento="CPF", numero_documento="471.693.820-72")

    c18 = Cidadao.objects.create(nome_pessoa="Rodrigo Rocha Almeida", estado_civil="DIVORCIADO", num_sus="9000015", data_nascimento="1984-04-15", genero="M", naturalidade="Juazeiro do Norte", ocupacao="Motorista", address=enderecos[15], ubs=ubs_list[3])
    Documento.objects.create(pessoa=c18, tipo_documento="CPF", numero_documento="520.483.716-09")

    c19 = Cidadao.objects.create(nome_pessoa="Débora Cristina Gomes", estado_civil="SOLTEIRO", num_sus="9000016", data_nascimento="1996-03-12", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Recepcionista", address=enderecos[25], ubs=ubs_list[3])
    Documento.objects.create(pessoa=c19, tipo_documento="CPF", numero_documento="634.981.257-11")

    c20 = Cidadao.objects.create(nome_pessoa="Sérgio Henrique Fernandes Souza", estado_civil="CASADO", num_sus="9000017", data_nascimento="1982-08-28", genero="M", naturalidade="Juazeiro do Norte", ocupacao="Pedreiro", address=enderecos[26], ubs=ubs_list[3])
    Documento.objects.create(pessoa=c20, tipo_documento="CPF", numero_documento="718.450.392-86")

    c21 = Cidadao.objects.create(nome_pessoa="Tatiane Alves Barbosa", estado_civil="SOLTEIRO", num_sus="9000018", data_nascimento="1994-06-18", genero="F", naturalidade="Juazeiro do Norte", ocupacao="Comerciante", address=enderecos[27], ubs=ubs_list[3])
    Documento.objects.create(pessoa=c21, tipo_documento="CPF", numero_documento="809.317.546-94")

    # =========================
    # UBS 4 (7453626)
    # =========================

    c22 = Cidadao.objects.create(nome_pessoa="Gabriel Luiz Pereira", estado_civil="CASADO", num_sus="9000019", data_nascimento="1981-07-22", genero="M", naturalidade="Crato", ocupacao="Agricultor", address=enderecos[4], ubs=ubs_list[4])
    Documento.objects.create(pessoa=c22, tipo_documento="CPF", numero_documento="903.845.271-33")

    c23 = Cidadao.objects.create(nome_pessoa="Larissa Santos Gomes", estado_civil="SOLTEIRO", num_sus="9000020", data_nascimento="1997-05-14", genero="F", naturalidade="Crato", ocupacao="Atendente", address=enderecos[30], ubs=ubs_list[4])
    Documento.objects.create(pessoa=c23, tipo_documento="CPF", numero_documento="124.690.538-47")

    c24 = Cidadao.objects.create(nome_pessoa="André Felipe Batista Oliveira", estado_civil="DIVORCIADO", num_sus="9000021", data_nascimento="1983-09-17", genero="M", naturalidade="Crato", ocupacao="Motorista", address=enderecos[4], ubs=ubs_list[4])
    Documento.objects.create(pessoa=c24, tipo_documento="CPF", numero_documento="236.481.759-82")

    c25 = Cidadao.objects.create(nome_pessoa="Patrícia Fernanda Barros Lima", estado_civil="SOLTEIRO", num_sus="9000022", data_nascimento="1991-12-10", genero="F", naturalidade="Crato", ocupacao="Costureira", address=enderecos[30], ubs=ubs_list[4])
    Documento.objects.create(pessoa=c25, tipo_documento="CPF", numero_documento="347.920.681-15")

    c26 = Cidadao.objects.create(nome_pessoa="Ricardo Augusto Farias Teixeira", estado_civil="CASADO", num_sus="9000023", data_nascimento="1986-05-02", genero="M", naturalidade="Crato", ocupacao="Pedreiro", address=enderecos[4], ubs=ubs_list[4])
    Documento.objects.create(pessoa=c26, tipo_documento="CPF", numero_documento="458.172.906-64")

    c27 = Cidadao.objects.create(nome_pessoa="Juliana Vitória Azevedo Mendes", estado_civil="SOLTEIRO", num_sus="9000024", data_nascimento="1994-07-25", genero="F", naturalidade="Crato", ocupacao="Vendedora", address=enderecos[30], ubs=ubs_list[4])
    Documento.objects.create(pessoa=c27, tipo_documento="CPF", numero_documento="569.381.742-28")


# from ubs.models import Documento, Pessoa

# def rodar():

#     for i in range(36, 66):
#         try:
#             pessoa = Pessoa.objects.get(id=i)

#             Documento.objects.create(
#                 pessoa=pessoa,
#                 tipo_documento="CPF",
#                 numero_documento=f"900.111.222-{i}"
#             )

#         except Pessoa.DoesNotExist:
#             print(f"Pessoa {i} não existe")


from ubs.models import Anamnese, Cidadao
from datetime import date

def seed_anamnese(): 
    dados = [
        (9000001, 78.5, 1.72, date(2026,3,10), '130/85'),
        (9000002, 62.3, 1.60, date(2026,3,11), '120/80'),
        (9000003, 55.0, 1.58, date(2026,3,12), '115/75'),
        (9000004, 68.2, 1.65, date(2026,3,13), '125/80'),
        (9500001, 3.2, 0.50, date(2026,3,2), '80/50'),
        (9500003, 22.0, 1.10, date(2026,3,5), '90/60'),

        (9000005, 85.0, 1.75, date(2026,3,10), '145/90'),
        (9000006, 64.0, 1.62, date(2026,3,11), '120/80'),
        (9000007, 59.0, 1.60, date(2026,3,12), '118/78'),
        (9000008, 70.0, 1.68, date(2026,3,13), '128/82'),

        (9700001, 21.0, 1.08, date(2026,3,9), '95/60'),
        (9700002, 19.5, 1.02, date(2026,3,8), '90/60'),

        (9000009, 90.0, 1.78, date(2026,3,10), '150/95'),
        (9000010, 58.0, 1.59, date(2026,3,11), '115/75'),
        (9000011, 60.0, 1.63, date(2026,3,12), '120/80'),
        (9000012, 82.0, 1.74, date(2026,3,13), '138/88'),

        (9000014, 65.0, 1.64, date(2026,3,10), '122/80'),
        (9000015, 88.0, 1.80, date(2026,3,11), '142/90'),
        (9000016, 55.0, 1.60, date(2026,3,12), '110/70'),
        (9000017, 79.0, 1.70, date(2026,3,13), '135/85'),

        (9000019, 84.0, 1.76, date(2026,3,10), '140/90'),
        (9000020, 61.0, 1.62, date(2026,3,11), '120/80'),
        (9000021, 87.0, 1.79, date(2026,3,12), '145/92'),
        (9000022, 63.0, 1.64, date(2026,3,13), '125/82'),
    ]

    objetos = []

    for num_sus, peso, altura, data, pa in dados:
        try:
            cidadao = Cidadao.objects.get(num_sus=num_sus)

            objetos.append(
                Anamnese(
                    cidadao=cidadao,
                    peso=peso,
                    altura=altura,
                    data_anamnese=data,
                    pressao_arterial=pa
                )
            )

        except Cidadao.DoesNotExist:
            print(f"⚠️ Cidadão com SUS {num_sus} não encontrado")

    Anamnese.objects.bulk_create(objetos)