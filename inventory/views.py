from django.shortcuts import render, get_object_or_404, redirect
from .models import Buku, Reservasi
from .forms import ReservasiForm


def index(request):
    query = request.GET.get('q', '')
    if query:
        buku_list = Buku.objects.filter(judul__icontains=query)
    else:
        buku_list = Buku.objects.all()
    return render(request, 'index.html', {'buku_list': buku_list})


def detail_buku(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    return render(request, 'detail.html', {'buku': buku})


def proses_reservasi(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    if buku.stok <= 0:
        return render(request, 'detail.html', {'buku': buku, 'error': 'Maaf, stok baru saja habis!'})
    if request.method == 'POST':
        form = ReservasiForm(request.POST)
        if form.is_valid():
            reservasi = form.save(commit=False)
            reservasi.buku = buku
            reservasi.save()
            return render(request, 'sukses.html', {'buku': buku})
    else:
        form = ReservasiForm()
    return render(request, 'reservasi_form.html', {'form': form, 'buku': buku})


def tentang(request):
    return render(request, 'about.html')
