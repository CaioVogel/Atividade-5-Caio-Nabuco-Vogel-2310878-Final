# Generated by Django 5.0.2 on 2024-04-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=80)),
                ('Icone', models.CharField(max_length=2000)),
                ('Descricao', models.TextField(blank=True)),
                ('Lancamento', models.DateField()),
                ('Diretor', models.CharField(max_length=80)),
                ('Critica_geral', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeL', models.CharField(choices=[('R', 'Rotten tomatoes'), ('I', 'IMDB')], max_length=1)),
                ('link', models.URLField(max_length=2000)),
                ('FK_NomeF', models.CharField(max_length=80)),
                ('Critica', models.DecimalField(decimal_places=1, max_digits=3)),
                ('QTDCritical', models.CharField(max_length=10)),
            ],
        ),
    ]