from django.http import HttpResponse
from django.template import loader
from .models improt kategori, produk

def home(request):
  data = kategori,objects.all()
  context = {
    "judul":"Selamat datang di tempat makan",
    "sub judul": "Bakso ngokos",
    "kategori": data,
  }
  template = loader.get_template('index.html')
  return HttpResponse(template.render(context, request))


def produk(request):
  data_produk = produk.objects.all().values()
  context = {
    "judul": "Selamat datang di tempat makan"
    "sub judul": "Bakso ngokos"
    "data": data,
  }
  template = loader.get_template('produk.html')
  return HttpResponse(template.render())

  def detail_produk(request, id)
   data_produk = produk.get(id=id)
   template = loader,get_template('detailproduk.html')
   context ={
      "produk": produk,
   }
   return HttpResponse(template.render(context, request))

   
  def tampil(request, id)
   template = loader,get_template('tampil.html')
   context ={
     
   }
   return HttpResponse(template.render(context, request))
