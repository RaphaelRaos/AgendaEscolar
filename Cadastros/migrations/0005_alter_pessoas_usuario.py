# Generated by Django 3.2.9 on 2021-11-22 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cadastros', '0004_rename_alunos_prescricoes_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='Usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]