# Generated by Django 4.1.7 on 2023-02-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minasul', '0002_tractor_identification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='cnh',
            field=models.CharField(max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='tractor',
            name='identification',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
