from django.urls import path
from . import views
app_name= 'sistemLinen'
from django.conf.urls import url
from.import views





urlpatterns = [
    path('', views.index, name='index'),
    path('/tambah_transaksi', views.tambah_transaksi, name=views.tambah_transaksi),
    path('tambah_detail_transaksi', views.tambah_detail_transaksi, name = views.tambah_detail_transaksi),
    path('<str:unit_id>/masukkan_detail_transaksi/', views.masukkan_detail_transaksi, namw = masukkan_detail_transaksi),
    path('masukkan_keranjang/', views.masukkan_keranjang, name = masukkan_keranjang)

]