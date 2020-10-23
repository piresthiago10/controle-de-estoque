# Generated by Django 3.1.2 on 2020-10-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('quantidade_estoque', models.IntegerField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produto')),
                ('categoria', models.OneToOneField(on_delete=models.SET('Categoria Excluída'), to='categoria.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]