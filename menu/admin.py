from django.contrib import admin
from .models improt produk, kategori

# Register your models here.


class produkAdmin(admin.ModelAdmin):
    list_display = ("namaproduk", "harga")


admin.site.register(kategori)
admin.site.register(produk , produkAdmin)