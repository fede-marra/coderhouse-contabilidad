# Generated by Django 4.0.5 on 2022-06-21 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_rename_detalle_ingreso_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='egreso',
            old_name='detalle',
            new_name='nombre',
        ),
    ]
