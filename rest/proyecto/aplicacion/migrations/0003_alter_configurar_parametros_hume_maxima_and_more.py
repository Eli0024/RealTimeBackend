# Generated by Django 5.0.7 on 2024-07-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_rename_confirmar_contraseña_usuario_confirmar_contrasena_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurar_parametros',
            name='hume_maxima',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configurar_parametros',
            name='hume_minima',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configurar_parametros',
            name='tem_maxima',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configurar_parametros',
            name='tem_minima',
            field=models.IntegerField(),
        ),
    ]
