# Create your models here.
class kategori(models.Model):
    nama = models.CharField(max_length=100)





    def __str__(self):
        return f"{self.nama}"

#admin.site.register(kategori)

class produk(models.Model):
    kategori = models.Foreignkey(kategori, on_delete=models.CASCADE)
    namaproduk = models.CharField(max_length=100)
    harga = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.namaproduk} {self.harga}"

# admin.site.register(produk)
