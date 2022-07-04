# Generated by Django 4.0.5 on 2022-06-28 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('ANALISES', 'Análises'), ('PROGRAMACAO', 'Programação'), ('APRESENTACAO', 'Apresentação'), ('OUTROS', 'Outros')], default='', max_length=15),
        ),
        migrations.AddField(
            model_name='filme',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filme',
            name='descrica',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='filme',
            name='thumb',
            field=models.ImageField(default='', upload_to='thumb_filmes'),
        ),
        migrations.AddField(
            model_name='filme',
            name='titulo',
            field=models.CharField(default='Titulo', max_length=100),
        ),
        migrations.AddField(
            model_name='filme',
            name='visualizacao',
            field=models.IntegerField(default=0),
        ),
    ]