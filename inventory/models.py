
from django.db import models
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    def __str__(self): return self.nama
class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    stok = models.PositiveIntegerField(default=1)
    gambar = models.ImageField(upload_to='buku/', blank=True, null=True)
    def __str__(self): return self.judul
class Reservasi(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    nama_peminjam = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='PENDING')
    email_peminjam = models.EmailField()
    def __str__(self): return f"{self.nama_peminjam} - {self.buku.judul} ({self.status})"