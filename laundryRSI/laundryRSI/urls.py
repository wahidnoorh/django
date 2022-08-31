
from django.contrib import admin
from sistemLinen import views as viewsLinen
from django.urls import path 
from . import views
app_name= 'sistemLinen'
from django.conf.urls import url
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',viewsLinen.index, name = 'index'),
     
    path('<int:keranjang_id>hapus_item_keranjang', viewsLinen.hapus_item_keranjang, name = 'hapus_item_keranjang'),

    path('<int:unit_id>tambah_detail_transaksi', viewsLinen.tambah_detail_transaksi, name = 'tambah_detail_transaksi'),
    path('<int:unit_id>/masukkan_keranjang/', viewsLinen.masukkan_keranjang, name = 'masukkan_keranjang'),
    path('masukkan_transaksi', viewsLinen.masukkan_transaksi, name = 'masukkan_transaksi'),
    path('validasi_transaksi', viewsLinen.validasi_transaksi, name = 'validasi_transaksi'),
    path('data_transaksi', viewsLinen.data_transaksi, name = 'data_transaksi'),
    path('<int:transaksi_id>/ubah_status_transaksi/', viewsLinen.ubah_status_transaksi, name='ubah_status_transaksi'),
    path('<int:transaksi_id>/tampilkan_transaksi/', viewsLinen.tampilkan_transaksi, name='tampilkan_transaksi'),
    path('login', viewsLinen.loginView, name='login'),
    path('logoutView', viewsLinen.logoutView, name='logoutView'),

    path('', viewsLinen.login_form, name='login_form')


]

urlpatterns += staticfiles_urlpatterns()