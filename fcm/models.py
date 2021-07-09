from django.db import models

# Create your models here.

class DataLatih(models.Model):
    nama_pemain = models.TextField()
    posisi = models.IntegerField()
