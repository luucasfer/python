# Generated by Django 4.1.7 on 2023-03-28 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tutor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, null=True, unique=True)),
                ("email", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=4, null=True)),
                ("phone", models.CharField(blank=True, max_length=30)),
                ("city", models.DateField(blank=True, max_length=30)),
                ("about", models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
