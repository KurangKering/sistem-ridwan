from django.db import models
from django.db.models.signals import pre_save
# Create your models here.

class DataLatihKiper(models.Model):
    nama = models.TextField()
    usia = models.IntegerField(default=0)
    pemain_inti = models.IntegerField(default=0)
    cadangan_main = models.IntegerField(default=0)
    mop = models.IntegerField(default=0)
    kk = models.IntegerField(default=0)
    km = models.IntegerField(default=0)
    gol = models.IntegerField(default=0)
    kemasukan = models.IntegerField(default=0)
    penyelamatan = models.IntegerField(default=0)
    norm_usia = models.FloatField(null=True, blank=True)
    norm_pemain_inti = models.FloatField(null=True, blank=True)
    norm_cadangan_main = models.FloatField(null=True, blank=True)
    norm_mop = models.FloatField(null=True, blank=True)
    norm_kk = models.FloatField(null=True, blank=True)
    norm_km = models.FloatField(null=True, blank=True)
    norm_gol = models.FloatField(null=True, blank=True)
    norm_kemasukan = models.FloatField(null=True, blank=True)
    norm_penyelamatan = models.FloatField(null=True, blank=True)

    def set_bobot_data(self):
        self.norm_usia = self.usia
        self.norm_pemain_inti = self.pemain_inti
        self.norm_cadangan_main = self.cadangan_main
        self.norm_mop = self.mop
        self.norm_kk = self.kk
        self.norm_km = self.km
        self.norm_gol = self.gol
        self.norm_kemasukan = self.kemasukan
        self.norm_penyelamatan = self.penyelamatan



