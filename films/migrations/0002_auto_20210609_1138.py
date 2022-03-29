# Generated by Django 3.2.4 on 2021-06-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(to='films.Actor'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='birthdate',
            field=models.DateField(),
        ),
    ]