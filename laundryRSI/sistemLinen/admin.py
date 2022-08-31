from django.contrib import admin

from sistemLinen.models import Unit_kerja, Status, Linen, Transaksi
from django.contrib import admin

from .models import Detail_transaksi, Keranjang, Unit_kerja, Status, Linen, Transaksi

admin.site.register(Unit_kerja),
admin.site.register(Status),
admin.site.register(Linen),
admin.site.register(Transaksi),
admin.site.register(Detail_transaksi),
admin.site.register(Keranjang)
