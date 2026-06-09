from django.shortcuts import render, get_object_or_404
from .models import Buku, Reservasi, Kategori
from .forms import ReservasiForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BukuSerializer


@api_view(['GET', 'POST'])
def api_books(request):

    if request.method == 'GET':
        books = Buku.objects.all()
        serializer = BukuSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BukuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'PUT', 'DELETE'])
def api_book_detail(request, pk):

    try:
        book = Buku.objects.get(pk=pk)
    except Buku.DoesNotExist:
        return Response(
            {"error": "Buku tidak ditemukan"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = BukuSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BukuSerializer(
            book,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        book.delete()

        return Response(
            {"message": "Buku berhasil dihapus"},
            status=status.HTTP_200_OK
        )


def index(request):
    query = request.GET.get('q', '')
    kategori_id = request.GET.get('kategori', '')

    buku_list = Buku.objects.all()
    kategori_list = Kategori.objects.all()

    if kategori_id:
        buku_list = buku_list.filter(kategori_id=kategori_id)

    if query:
        buku_list = buku_list.filter(judul__icontains=query)

    context = {
        'buku_list': buku_list,
        'kategori_list': kategori_list,
        'query': query,
        'kategori_aktif': kategori_id,
    }

    return render(request, 'index.html', context)


def detail_buku(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    return render(request, 'detail.html', {'buku': buku})


def proses_reservasi(request, pk):
    buku = get_object_or_404(Buku, pk=pk)

    if buku.stok <= 0:
        return render(
            request,
            'detail.html',
            {
                'buku': buku,
                'error': 'Maaf, stok baru saja habis!'
            }
        )

    if request.method == 'POST':
        form = ReservasiForm(request.POST)

        if form.is_valid():
            reservasi = form.save(commit=False)
            reservasi.buku = buku
            reservasi.save()

            return render(
                request,
                'sukses.html',
                {'buku': buku}
            )

    else:
        form = ReservasiForm()

    return render(
        request,
        'reservasi_form.html',
        {
            'form': form,
            'buku': buku
        }
    )


def tentang(request):
    return render(request, 'about.html')