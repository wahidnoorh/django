from datetime import datetime
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
from django.db import models
from django.db.models.base import Model

class Status(models.Model):
    def __str__(self):
        return (self.nama)
        
    nama = models.CharField(max_length= 24, default= '') 
class Unit_kerja(models.Model):
    
    nama_unit = models.CharField(max_length=25)
    jenis_linen = models.ManyToManyField(Status )
    def __str__(self): 
        return (self.nama_unit)
   
class Linen (models.Model): 
    def __str__(self):
        return (self.nama)
    nama = models.CharField( max_length= 24,default = '')
    status = models.ForeignKey (Status, on_delete=models.CASCADE)
    
class Transaksi(models.Model):
    Unit = models.ForeignKey(Unit_kerja, on_delete=models.CASCADE)
    Linen = models.ManyToManyField(Linen, through= 'Detail_transaksi')
    def __str__(self): 
        return ( str(self.id))
    status_konfirmasi = models.BooleanField (default= False)
    waktu_masuk = models.DateTimeField(default= datetime.datetime.now)
    waktu_keluar = models.DateTimeField(null=True)

class Detail_transaksi(models.Model):
    Transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    Linen = models.ForeignKey(Linen, on_delete=models.CASCADE)
    jumlah = models.IntegerField( blank= True, null= True)
    waktu = models.DateTimeField()

class Keranjang (models.Model):
    transaksi = models.IntegerField()
    linen = models.CharField(max_length= 20)
    jumlah = models.IntegerField ()
    waktu = models.DateTimeField()
