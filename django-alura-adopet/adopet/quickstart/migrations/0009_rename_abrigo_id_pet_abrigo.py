# Generated by Django 4.2 on 2023-04-05 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quickstart", "0008_pet_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pet", old_name="abrigo_id", new_name="abrigo",
        ),
    ]
