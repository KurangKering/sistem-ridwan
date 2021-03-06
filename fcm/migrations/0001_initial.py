# Generated by Django 3.2.5 on 2021-07-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataLatih',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField()),
                ('usia', models.IntegerField(default=0, max_length=6)),
                ('pemain_inti', models.IntegerField(default=0, max_length=6)),
                ('cadangan_main', models.IntegerField(default=0, max_length=6)),
                ('mop', models.IntegerField(default=0, max_length=6)),
                ('kk', models.IntegerField(default=0, max_length=6)),
                ('km', models.IntegerField(default=0, max_length=6)),
                ('gol', models.IntegerField(default=0, max_length=6)),
                ('kemasukan', models.IntegerField(default=0, max_length=6)),
                ('penyelamatan', models.IntegerField(default=0, max_length=6)),
                ('norm_usia', models.FloatField(blank=True, null=True)),
                ('norm_pemain_inti', models.FloatField(blank=True, null=True)),
                ('norm_cadangan_main', models.FloatField(blank=True, null=True)),
                ('norm_mop', models.FloatField(blank=True, null=True)),
                ('norm_kk', models.FloatField(blank=True, null=True)),
                ('norm_km', models.FloatField(blank=True, null=True)),
                ('norm_gol', models.FloatField(blank=True, null=True)),
                ('norm_kemasukan', models.FloatField(blank=True, null=True)),
                ('norm_penyelamatan', models.FloatField(blank=True, null=True)),
                ('posisi', models.IntegerField()),
            ],
        ),
    ]
