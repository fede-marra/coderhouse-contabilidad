# Generated by Django 4.0.5 on 2022-06-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_egreso', '0005_remove_persona_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(default='Ingresar apellido', max_length=30),
            preserve_default=False,
        ),
    ]