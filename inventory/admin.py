from django.contrib import admin
from .models import Buku, Kategori, Reservasi

@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis', 'stok', 'kategori')
    list_filter = ('kategori',)
    search_fields = ('judul',)

@admin.register(Reservasi)
class ReservasiAdmin(admin.ModelAdmin):
    # Menampilkan kolom status agar enak dilihat
    list_display = ('nama_peminjam', 'buku', 'email_peminjam', 'status')
    list_filter = ('status',)
    
    # --- INI LOGIKA PINTARNYA ---
    actions = ['setujui_peminjaman', 'batalkan_peminjaman', 'kembalikan_buku']

    def setujui_peminjaman(self, request, queryset):
        for res in queryset:
            if res.status == 'PENDING':
                if res.buku.stok > 0:
                    res.buku.stok -= 1 # Kurangi stok otomatis
                    res.buku.save()
                    res.status = 'DISETUJUI'
                    res.save()
                else:
                    self.message_user(request, f"Gagal: Stok {res.buku.judul} habis!")
        self.message_user(request, "Berhasil menyetujui reservasi dan mengurangi stok.")
    
    setujui_peminjaman.short_description = "Setujui & Kurangi Stok Otomatis"

    def batalkan_peminjaman(self, request, queryset):
        for res in queryset:
            if res.status == 'PENDING':
                res.status = 'DIBATALKAN'
                res.save()
        self.message_user(request, "Berhasil membatalkan reservasi.")

    def kembalikan_buku(self, request, queryset):
      for res in queryset:
        if res.status == 'DISETUJUI':
            res.buku.stok += 1 # Tambah stok kembali
            res.buku.save()
            res.status = 'KEMBALI'
            res.save()
    kembalikan_buku.short_description = "Buku Kembali (Tambah Stok)"

admin.site.register(Kategori)