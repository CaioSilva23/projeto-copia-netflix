# Generated by Django 4.0.5 on 2022-06-29 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0004_rename_episodios_episodio'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='titulo',
            field=models.CharField(default='Titulo', max_length=100),
        ),
        migrations.AddField(
            model_name='episodio',
            name='video',
            field=models.URLField(default=''),
        ),
    ]
