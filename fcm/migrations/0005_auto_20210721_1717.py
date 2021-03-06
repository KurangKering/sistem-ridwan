# Generated by Django 3.2.5 on 2021-07-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcm', '0004_remove_datalatihkiper_posisi'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataLatihPemain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField()),
                ('usia', models.IntegerField(default=0)),
                ('pemain_inti', models.IntegerField(default=0)),
                ('cadangan_main', models.IntegerField(default=0)),
                ('mop', models.IntegerField(default=0)),
                ('kk', models.IntegerField(default=0)),
                ('km', models.IntegerField(default=0)),
                ('gol', models.IntegerField(default=0)),
                ('kemasukan', models.IntegerField(default=0)),
                ('penyelamatan', models.IntegerField(default=0)),
                ('assist', models.IntegerField(default=0)),
                ('pelanggaran', models.IntegerField(default=0)),
                ('dilanggar_lawan', models.IntegerField(default=0)),
                ('akurasi_tembakan', models.IntegerField(default=0)),
                ('akurasi_operan', models.IntegerField(default=0)),
                ('akurasi_umpan_silang', models.IntegerField(default=0)),
                ('sukses_tekel', models.IntegerField(default=0)),
                ('sukses_dribel', models.IntegerField(default=0)),
                ('posisi', models.IntegerField()),
                ('norm_usia', models.FloatField(blank=True, null=True)),
                ('norm_pemain_inti', models.FloatField(blank=True, null=True)),
                ('norm_cadangan_main', models.FloatField(blank=True, null=True)),
                ('norm_mop', models.FloatField(blank=True, null=True)),
                ('norm_kk', models.FloatField(blank=True, null=True)),
                ('norm_km', models.FloatField(blank=True, null=True)),
                ('norm_gol', models.FloatField(blank=True, null=True)),
                ('norm_kemasukan', models.FloatField(blank=True, null=True)),
                ('norm_penyelamatan', models.FloatField(blank=True, null=True)),
                ('norm_assist', models.FloatField(blank=True, null=True)),
                ('norm_pelanggaran', models.FloatField(blank=True, null=True)),
                ('norm_dilanggar_lawan', models.FloatField(blank=True, null=True)),
                ('norm_akurasi_tembakan', models.FloatField(blank=True, null=True)),
                ('norm_akurasi_operan', models.FloatField(blank=True, null=True)),
                ('norm_akurasi_umpan_silang', models.FloatField(blank=True, null=True)),
                ('norm_sukses_tekel', models.FloatField(blank=True, null=True)),
                ('norm_sukses_dribel', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DataLatihKiper',
        ),
    ]
