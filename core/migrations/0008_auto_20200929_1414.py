# Generated by Django 3.1.1 on 2020-09-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200929_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='dia',
            field=models.DateField(verbose_name='Dia'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='horario',
            field=models.TimeField(verbose_name='Horário'),
        ),
    ]
