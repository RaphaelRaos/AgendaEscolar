"""
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
"""
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.models import User
from localflavor.br.models import BRCPFField

# Create your models here.

# Nivel 0 Alimentos
class Alimentos(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Alimento_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Alimento_id",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    Descricao = models.CharField(
        max_length=150,
        verbose_name="Descrição",
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.Nome}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Alimentos"
        ordering = ("Nome",)
        verbose_name = "Alimento"
        UniqueConstraint(fields=["Alimento_id"], name="AlimentosPK")
        UniqueConstraint(fields=["Nome"], name="AlimentosAK")


# Nivel 0 Itens
class Itens(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Item_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Item_id",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    Descricao = models.CharField(
        max_length=150,
        verbose_name="Descrição",
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.Nome}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Itens"
        ordering = ("Nome",)
        verbose_name = "Item"
        UniqueConstraint(fields=["Item_id"], name="ItensPK")
        UniqueConstraint(fields=["Nome"], name="ItensAK")


# Nivel 0 Medicamentos
class Medicamentos(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Medicamento_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Medicamento_id",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    Descricao = models.CharField(
        max_length=150,
        verbose_name="Descrição",
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.Nome}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Medicamentos"
        ordering = ("Nome",)
        verbose_name = "Medicamento"
        UniqueConstraint(fields=["Medicamento_id"], name="MedicamentosPK")
        UniqueConstraint(fields=["Nome"], name="MedicamentosAK")


# Nivel 0 Pessoas
class Pessoas(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Pessoa_id = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="Pessoa_id"
    )
    Usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    Nome = models.CharField(
        max_length=50,
        verbose_name="Nome",
        blank=False,
        null=True,
        unique=True,
    )
    Apelido = models.CharField(
        max_length=50,
        verbose_name="Apelido",
        blank=False,
        null=True,
        unique=False,
    )
    DataNascimento = models.DateField(verbose_name="Data de Nascimento", null=True)
    Telefone = models.CharField(max_length=16, null=True)
    CPF = BRCPFField(verbose_name="CPF", null=True)
    RG = models.CharField(verbose_name="RG", max_length=11, null=True)

    def __str__(self):
        return f"{self.Apelido} ({self.Nome})"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Pessoas"
        ordering = ("Nome",)
        verbose_name = "Pessoa"
        UniqueConstraint(fields=["Pesoa_id"], name="PessoasAK")
        UniqueConstraint(fields=["Nome"], name="PessoasAK")


# Nivel 0 Turmas
class Turmas(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    TurmaId = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="TurmaId"
    )
    Nome = models.CharField(
        max_length=50,
        verbose_name="Nome",
        blank=False,
        null=False,
        unique=True,
    )
    AnoLetivo = models.IntegerField(verbose_name="Ano Letivo")
    AnoEscolar = models.IntegerField(verbose_name="Ano Escolar")

    def __str__(self):
        return f"{self.Nome}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Turmas"
        ordering = ("AnoLetivo", "AnoEscolar")
        verbose_name = "Turma"
        UniqueConstraint(fields=["TurmaId"], name="TurmasPK")
        UniqueConstraint(fields=["Nome"], name="TurmasAK")


# Nivel 1 Alunos
class Alunos(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Aluno_id = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="Aluno_id"
    )
    Pessoa = models.OneToOneField(Pessoas, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Pessoa}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Alunos"
        verbose_name = "Aluno"
        UniqueConstraint(fields=["Aluno_id"], name="AlunosPK")
        UniqueConstraint(fields=["Pessoa"], name="AlunosAK")


# Nivel 1 Professores
class Professores(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Professor_id = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="Professor_id"
    )
    Pessoa = models.OneToOneField(Pessoas, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Pessoa}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Professores"
        verbose_name = "Professor"
        UniqueConstraint(fields=["Professor_id"], name="ProfessorPK")
        UniqueConstraint(fields=["Pessoa"], name="ProfessorAK")


# Nivel 1 Responsaveis
class Responsaveis(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Responsavel_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Responsavel_id",
    )
    Pessoa = models.OneToOneField(Pessoas, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Pessoa}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Responsaveis"
        verbose_name = "Responsavel"
        UniqueConstraint(fields=["Responsavel_id"], name="ResponsavelPK")
        UniqueConstraint(fields=["Pessoa"], name="ResponsavelAK")


# Nivel 2 ResponsaveisAlunos
class ResponsaveisAlunos(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    ResponsavelAluno_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="ResponsavelAluno_id",
    )
    Responsavel = models.ForeignKey(
        Responsaveis, db_index=True, on_delete=models.PROTECT
    )
    Aluno = models.ForeignKey(Alunos, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Responsavel}:{self.Aluno}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "ResponsaveisAlunos"
        verbose_name = "ResponsavelAluno"
        UniqueConstraint(fields=["ResponsavelAluno_id"], name="ResponsavelAlunoPK")


# Nivel 2 Matriculas
class Matriculas(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Matricula_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Matricula_id",
    )
    Turma = models.ForeignKey(Turmas, db_index=True, on_delete=models.PROTECT)
    Aluno = models.ForeignKey(Alunos, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Turma}:{self.Aluno}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Matriculas"
        verbose_name = "Matrículas"
        UniqueConstraint(fields=["Matricula_id"], name="MatriculaPK")


# Nivel 2 TurmasProfessores
class TurmasProfessores(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    TurmaProfessor_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Matricula_id",
    )
    Turma = models.ForeignKey(Turmas, db_index=True, on_delete=models.PROTECT)
    Professor = models.ForeignKey(Professores, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Turma}:{self.Professor}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "TurmasProfessores"
        verbose_name = "Professores por Turma"
        UniqueConstraint(fields=["TurmaProfessor_id"], name="TurmaProfessorPK")


# Nivel 2 Prescricoes
class Prescricoes(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Prescricao_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Matricula_id",
    )
    Aluno = models.ForeignKey(Alunos, db_index=True, on_delete=models.PROTECT)
    Medicamento = models.ForeignKey(
        Medicamentos, db_index=True, on_delete=models.PROTECT
    )
    DataInicial = models.DateField(null=False, blank=False)
    DataFinal = models.DateField(null=False, blank=False)
    Posologia = models.TextField(blank=False, null=False)
    Horarios = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.Aluno}:{self.Medicamento}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Prescricoes"
        verbose_name = "Prescrições"
        UniqueConstraint(fields=["Prescricao_id"], name="PrescricaoPK")


# Nivel 3 Agendas
class Agendas(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Agenda_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Agenda_id",
    )
    TurmaProfessor = models.ForeignKey(
        TurmasProfessores, db_index=True, on_delete=models.PROTECT
    )
    Matricula = models.ForeignKey(Matriculas, db_index=True, on_delete=models.PROTECT)
    Data = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.TurmaProfessor}:{self.Matricula}:{self.Data}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "Agendas"
        verbose_name = "Agendas"
        UniqueConstraint(fields=["Agenda_id"], name="AgendaPK")
        UniqueConstraint(fields=["TurmaProfessor", "Aluno", "Data"], name="AgendaAK")


# Nivel 4 AgendasAlimentos
class AgendasAlimentos(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Aceite = (
        ("O", "Ótimo"),
        ("R", "Regular"),
        ("G", "Rejeitou"),
    )

    AgendaAlimento_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaAlimento_id",
    )
    Agenda = models.ForeignKey(Agendas, db_index=True, on_delete=models.CASCADE)
    DiaHoraRegistro = models.DateTimeField(auto_now_add=True)
    Alimento = models.ForeignKey(Alimentos, db_index=True, on_delete=models.PROTECT)
    Aceite = models.CharField(max_length=1, choices=Aceite, default=Aceite[1][0])
    Hora = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.Agenda}:{self.Alimento}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "AgendasAlimentos"
        verbose_name = "Alimentos da Agenda"
        UniqueConstraint(fields=["AgendaAlimento_id"], name="AgendaAlimentoPK")


# Nivel 4 AgendasBanhos
class AgendasBanhos(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    AgendaBanho_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaBanho_id",
    )
    Agenda = models.ForeignKey(Agendas, db_index=True, on_delete=models.CASCADE)
    DiaHoraRegistro = models.DateTimeField(auto_now_add=True)
    Hora = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.Agenda}:{self.Hora}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "AgendasBanhos"
        verbose_name = "Banhos da Agenda"
        UniqueConstraint(fields=["AgendaBanho_id"], name="AgendaBanhoPK")


# Nivel 4 AgendasFisiologias
class AgendasFisiologias(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    Fisiologia = (
        ("F", "Fralda"),
        ("U", "Urina"),
        ("Z", "Fezes"),
        ("V", "Vômito"),
    )
    AgendaAlimento_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaFisiologia_id",
    )
    Agenda = models.ForeignKey(Agendas, db_index=True, on_delete=models.CASCADE)
    DiaHoraRegistro = models.DateTimeField(auto_now_add=True)
    Fisiologia = models.CharField(
        max_length=1, choices=Fisiologia, default=Fisiologia[0][0]
    )
    Hora = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.Agenda}:{self.Hora}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "AgendasFisiologias"
        verbose_name = "Fisiologias da Agenda"
        UniqueConstraint(fields=["AgendaFisiologia_id"], name="AgendaFisiologiaPK")


# Nivel 4 AgendasItens
class AgendasItens(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    AgendaAlimento_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaItem_id",
    )
    Agenda = models.ForeignKey(Agendas, db_index=True, on_delete=models.CASCADE)
    DiaHoraRegistro = models.DateTimeField(auto_now_add=True)
    Item = models.ForeignKey(Itens, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Agenda}:{self.Item}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "AgendasItens"
        verbose_name = "Itens da Agenda"
        UniqueConstraint(fields=["AgendaItem_id"], name="AgendaItemPK")


# Nivel 4 AgendasMedicamentos
class AgendasMedicamentos(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    AgendaMedicamento_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaMedicamento_id",
    )
    Agenda = models.ForeignKey(Agendas, db_index=True, on_delete=models.CASCADE)
    DiaHoraRegistro = models.DateTimeField(auto_now_add=True)
    Prescricao = models.ForeignKey(Prescricoes, db_index=True, on_delete=models.PROTECT)
    Hora = models.TimeField(null=False, blank=False)
    PosologiaAdministrada = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Agenda}:{self.Hora}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "AgendasMedicamentos"
        verbose_name = "Medicamentos da Agenda"
        UniqueConstraint(fields=["AgendaMedicamento_id"], name="AgendaMedicamentoPK")


# Nivel 4 AgendasRecados
class AgendasRecados(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    AgendaRecado_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaRecado_id",
    )
    Agenda = models.ForeignKey(Agendas, db_index=True, on_delete=models.CASCADE)
    DiaHoraRegistro = models.DateTimeField(auto_now_add=True)
    Recado = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.Agenda}:{self.Recado}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "AgendasRecados"
        verbose_name = "Recados da Agenda"
        UniqueConstraint(fields=["AgendaRecado_id"], name="AgendaRecadoPK")


# Nivel 4 AgendasSonos
class AgendasSonos(models.Model):
    """
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
    """

    AgendaSono_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaSono_id",
    )
    Agenda = models.ForeignKey(Agendas, db_index=True, on_delete=models.CASCADE)
    DiaHoraRegistro = models.DateTimeField(auto_now_add=True)
    Inicio = models.TimeField(null=False, blank=False)
    Fim = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.Agenda}:{self.Inicio}"

    class Meta:  # pylint: disable=too-few-public-methods
        """
        [summary]
        [extended_summary]
        Returns:
            [type]: [description]
        """

        db_table = "AgendasSonos"
        verbose_name = "Sonos da Agenda"
        UniqueConstraint(fields=["AgendaSono_id"], name="AgendaSonoPK")
