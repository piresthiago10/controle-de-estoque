# Generated by Django 3.1.2 on 2020-10-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20201023_1420'),
        ('estoque_saida', '0002_auto_20201023_1420'),
        ('produto', '0002_auto_20201023_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoquesaida',
            name='produto',
            field=models.OneToOneField(on_delete=models.SET('Produto descontinuado'), to='produto.produto'),
        ),
        migrations.AddField(
            model_name='estoquesaida',
            name='usuario',
            field=models.OneToOneField(on_delete=models.SET('Usuário Excluído'), to='usuario.usuario'),
        ),
    ]