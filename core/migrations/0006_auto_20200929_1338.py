# Generated by Django 3.1.1 on 2020-09-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_agendas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendas',
            name='horario',
            field=models.DateTimeField(editable=False, verbose_name='Horário'),
        ),
    ]
