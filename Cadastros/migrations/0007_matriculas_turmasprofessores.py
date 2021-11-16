# Generated by Django 3.2.9 on 2021-11-16 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastros', '0006_responsaveisalunos'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmasProfessores',
            fields=[
                ('TurmaProfessor_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Matricula_id')),
                ('Professor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cadastros.professores')),
                ('Turma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cadastros.turmas')),
            ],
            options={
                'verbose_name': 'Professores por Turma',
                'db_table': 'TurmasProfessores',
            },
        ),
        migrations.CreateModel(
            name='Matriculas',
            fields=[
                ('Matricula_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Matricula_id')),
                ('Aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cadastros.alunos')),
                ('Turma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cadastros.turmas')),
            ],
            options={
                'verbose_name': 'Matrículas',
                'db_table': 'Matriculas',
            },
        ),
    ]
