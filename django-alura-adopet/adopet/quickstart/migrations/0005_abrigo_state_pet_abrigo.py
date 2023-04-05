# Generated by Django 4.2 on 2023-04-04 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quickstart", "0004_abrigo_pet"),
    ]

    operations = [
        migrations.AddField(
            model_name="abrigo",
            name="state",
            field=models.CharField(default=None, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pet",
            name="abrigo",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.RESTRICT,
                to="quickstart.abrigo",
            ),
            preserve_default=False,
        ),
    ]