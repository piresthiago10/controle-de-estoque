# Generated by Django 3.1.2 on 2020-10-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20201023_1429'),
        ('usuario', '0002_auto_20201023_1420'),
        ('estoque_entrada', '0003_auto_20201023_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueentrada',
            name='produto',
            field=models.ForeignKey(on_delete=models.SET('Produto descontinuado'), to='produto.produto'),
        ),
        migrations.AlterField(
            model_name='estoqueentrada',
            name='usuario',
            field=models.ForeignKey(on_delete=models.SET('Usuário Excluído'), to='usuario.usuario'),
        ),
    ]