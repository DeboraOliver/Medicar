# Generated by Django 3.1.1 on 2020-09-29 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200929_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateTimeField(verbose_name='Dia')),
                ('horario', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Horário')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medico')),
            ],
        ),
        migrations.DeleteModel(
            name='Agendas',
        ),
    ]
