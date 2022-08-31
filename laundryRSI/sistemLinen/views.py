from django import template
import django
from sistemLinen.models import Transaksi
import xlwt
from django.shortcuts import render ,redirect
from django.template.loader import render_to_string
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Detail_transaksi, Unit_kerja, Status, Linen, Transaksi, Keranjang




def login_form(request):
    return render(request, 'login.html')


def loginView( request):
    if request.method == "POST":
        username_user = request.POST['username']
        password_user = request.POST['pswd']
        user = authenticate(request, username = username_user ,password = password_user) 
        print (user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect ("index")
        else:
            return HttpResponseRedirect("login_form")     
    return HttpResponseRedirect('index')

@login_required
def logoutView( request):
    logout(request)
    return redirect( 'login_form')
    
@login_required
def index(request):
    list_unit = Unit_kerja.objects.order_by()
    context = {'list_unit' : list_unit }
    return render(request, 'index.html', context)

             

@login_required
def masukkan_transaksi(request):
    unity = request.POST['unit_kerja']
    a = Unit_kerja.objects.get(nama_unit = unity)
    unit_id = a.id 
    input_transaksi = Transaksi(
    Unit = a                           )
    input_transaksi.save()
    return redirect ('tambah_detail_transaksi', unit_id = unit_id)


@login_required
def tambah_detail_transaksi (request, unit_id):
    unit_id = unit_id 
    a = Unit_kerja.objects.get(id = unit_id)
    
    tr = Transaksi.objects.last()
    unt = a
    jenis_linen = unt.jenis_linen.all()
    b = Transaksi.objects.values_list('Unit', flat=True)
    infeksius = Linen.objects.filter(status = 1)
    non_infeksius = Linen.objects.filter(status = 2)
    operasi = Linen.objects.filter(status = 3)
    keranjang = Keranjang.objects.all()
    keranjang1 = keranjang[::-1]
    unit = a
    context = {'unit': unit,
                'jenis_linen' : jenis_linen,
                'keranjang1': keranjang1,
                'infeksius' : infeksius,
                'non_infeksius': non_infeksius,
                'operasi' : operasi
              }
    return render( request, 'tambah_detail_transaksi.html', context)

@login_required
def masukkan_keranjang (request, unit_id ):
    unit_id = unit_id
    obj = Transaksi.objects.last()
    transaksi = obj.id

    tr = Keranjang( transaksi = transaksi,
                    linen = (request.POST['nama_linen']),
                    jumlah = (request.POST['jumlah']),
                    waktu = timezone.now()
                   )
    tr.save()
    unt = obj.Unit.jenis_linen.all()
    jenis_linen = unt
    infeksius = Linen.objects.filter(status = 1)
    non_infeksius = Linen.objects.filter(status = 2)
    operasi = Linen.objects.filter(status = 3)
    keranjang = Keranjang.objects.all()
    keranjang1= keranjang.reverse()
    

    return redirect ('tambah_detail_transaksi', unit_id = unit_id)

@login_required
def hapus_item_keranjang(request, keranjang_id):


    keranjang_id = keranjang_id
    item = Keranjang.objects.get(id = keranjang_id)
    transaksi = item.transaksi
    transaksi_object = Transaksi.objects.get(id = transaksi)
    unit_id = transaksi_object.Unit_id

    print (unit_id)
    item = Keranjang.objects.get(id = keranjang_id)
    item.delete()


    return redirect (tambah_detail_transaksi, unit_id = unit_id)

@login_required
def validasi_transaksi(request):
    keranjang = Keranjang.objects.all()

    for i in keranjang:
        insert = Detail_transaksi( Transaksi = Transaksi.objects.get(pk = i.transaksi),
                        Linen = Linen.objects.get(nama  = i.linen),
                        jumlah = i.jumlah,
                        waktu = i.waktu 
                        )        
        insert.save()
    cart = Keranjang.objects.all()
    cart.delete()
    list_unit = Unit_kerja.objects.order_by()
    context = {'list_unit' : list_unit }
    return render(request, 'index.html', context)

@login_required
def data_transaksi(request):
    data = Transaksi.objects.all()
    data = data[::-1]
    context = {
        'data': data ,   
    }
    return render(request, 'daftar_transaksi.html', context )  


@login_required
def ubah_status_transaksi(request, transaksi_id):
    transaksi = Transaksi.objects.get(pk = transaksi_id)
    transaksi.status_konfirmasi = True
    transaksi.save()
    transaksi.waktu_keluar = timezone.now()
    transaksi.save()
    data = Transaksi.objects.all()
    
    return redirect('data_transaksi') 
@login_required
def tampilkan_transaksi(request, transaksi_id):
    id_transaksi = transaksi_id
    list_transaksi = Detail_transaksi.objects.filter(Transaksi = id_transaksi)
    context = { 'list_transaksi' : list_transaksi}
    return render(request, 'tampilkan_transaksi.html', context )   




                

                           
