# Generated by Django 2.1.3 on 2019-05-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_auto_20190509_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='tiempo',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='tiempo_max',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='tiempo_min',
            field=models.TimeField(default='00:00:00'),
        ),
    ]