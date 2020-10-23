# Generated by Django 3.1.2 on 2020-10-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_usuario', '0002_auto_20201023_1420'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('login', models.CharField(max_length=60)),
                ('senha', models.CharField(max_length=32)),
                ('tipo_usuario', models.OneToOneField(on_delete=models.SET('Classificação Excluída'), to='tipo_usuario.tipousuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
