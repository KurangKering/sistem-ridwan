from django.db import models
from django.db.models.signals import pre_save
# Create your models here.

class DataLatihPemain(models.Model):
    nama = models.TextField()
    usia = models.IntegerField(default=0)
    pemain_inti = models.IntegerField(default=0)
    cadangan_main = models.IntegerField(default=0)
    mop = models.IntegerField(default=0)
    kk = models.IntegerField(default=0)
    km = models.IntegerField(default=0)
    gol = models.IntegerField(default=0)
    #field kemasukan dan & penyelamatan khusus posisi kiper
    kemasukan = models.IntegerField(default=0)
    penyelamatan = models.IntegerField(default=0)
    #field assist, pelanggaran, dilanggar_lawan, akurasi_tembakan, akurasi_operan, akurasi_umpan_silang khusus posisi pemain belakang, tengah, dan depan
    assist = models.IntegerField(default=0)
    pelanggaran = models.IntegerField(default=0)
    dilanggar_lawan = models.IntegerField(default=0)
    akurasi_tembakan = models.IntegerField(default=0)
    akurasi_operan = models.IntegerField(default=0)
    akurasi_umpan_silang = models.IntegerField(default=0)
    #field sukses_tekel khusus posisi pemain belakang
    sukses_tekel = models.IntegerField(default=0)
    #field sukses_dribel khusus posisi pemain tengah dan pemain depan
    sukses_dribel = models.IntegerField(default=0)
    #data posisi
    # 1 -> kiper
    # 2 -> pemain belakang
    # 3 -> pemain tengah
    # 4 -> pemain depan
    posisi = models.IntegerField()



    norm_usia = models.FloatField(null=True, blank=True)
    norm_pemain_inti = models.FloatField(null=True, blank=True)
    norm_cadangan_main = models.FloatField(null=True, blank=True)
    norm_mop = models.FloatField(null=True, blank=True)
    norm_kk = models.FloatField(null=True, blank=True)
    norm_km = models.FloatField(null=True, blank=True)
    norm_gol = models.FloatField(null=True, blank=True)
    norm_kemasukan = models.FloatField(null=True, blank=True)
    norm_penyelamatan = models.FloatField(null=True, blank=True)
    norm_assist = models.FloatField(null=True, blank=True)
    norm_pelanggaran = models.FloatField(null=True, blank=True)
    norm_dilanggar_lawan = models.FloatField(null=True, blank=True)
    norm_akurasi_tembakan = models.FloatField(null=True, blank=True)
    norm_akurasi_operan = models.FloatField(null=True, blank=True)
    norm_akurasi_umpan_silang = models.FloatField(null=True, blank=True)
    norm_sukses_tekel = models.FloatField(null=True, blank=True)
    norm_sukses_dribel = models.FloatField(null=True, blank=True)

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
        self.norm_assist = self.assist
        self.norm_pelanggaran = self.pelanggaran
        self.norm_dilanggar_lawan = self.dilanggar_lawan
        self.norm_akurasi_tembakan = self.akurasi_tembakan
        self.norm_akurasi_operan = self.akurasi_operan
        self.norm_akurasi_umpan_silang = self.akurasi_umpan_silang
        self.norm_sukses_tekel = self.sukses_tekel
        self.norm_sukses_dribel = self.sukses_dribel

    @classmethod
    def get_posisi_kiper(cls):
        return DataLatihPemain.objects.filter(posisi=1)

    @classmethod
    def get_posisi_belakang(cls):
        return DataLatihPemain.objects.filter(posisi=2)

    @classmethod
    def get_posisi_tengah(cls):
        return DataLatihPemain.objects.filter(posisi=3)

    @classmethod
    def get_posisi_depan(cls):
        return DataLatihPemain.objects.filter(posisi=4)

