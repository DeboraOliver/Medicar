# Generated by Django 3.1.1 on 2020-09-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200929_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='dia',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='horario',
            field=models.TimeField(),
        ),
    ]
