# Generated by Django 3.1.2 on 2020-10-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_usuario', '0002_auto_20201023_1420'),
        ('usuario', '0002_auto_20201023_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ForeignKey(on_delete=models.SET('Classificação Excluída'), to='tipo_usuario.tipousuario'),
        ),
    ]
