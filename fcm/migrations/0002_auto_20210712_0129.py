# Generated by Django 3.2.5 on 2021-07-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalatih',
            name='cadangan_main',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datalatih',
            name='gol',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datalatih',
            name='kemasukan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datalatih',
            name='kk',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datalatih',
            name='km',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datalatih',
            name='mop',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datalatih',
            name='pemain_inti',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datalatih',
            name='penyelamatan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datalatih',
            name='usia',
            field=models.IntegerField(default=0),
        ),
    ]