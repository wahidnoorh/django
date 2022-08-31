from django.db import models


class Unit_kerja(models.Model):
    def __str__(self): 
        return (self.nama_unit)
    nama_unit = models.CharField(max_length=25)

    
    
class Linen_regular(models.Model):
    def __str__(self):
        return str(self.masuk)
    Unit = models.ForeignKey(Unit_kerja, on_delete=models.CASCADE)
    Sprei = models.IntegerField( default=0 )
    Sarung_bantal = models.IntegerField( default=0 )
    pakaian_pasien = models.IntegerField( default=0 )
    korden = models.IntegerField( default=0 )
    taplak = models.IntegerField( default=0 )

class Ruang_operasi(models.Model):
    def __str__(self):
        return str(self.masuk)
    Unit = models.ForeignKey(Unit_kerja, on_delete=models.CASCADE)
    Sprei = models.IntegerField( default=0 )
    Sarung_bantal = models.IntegerField( default=0 )
    pakaian_pasien = models.IntegerField( default=0 )
    korden = models.IntegerField( default=0 )
    taplak = models.IntegerField( default=0 )
    
