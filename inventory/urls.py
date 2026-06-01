from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buku/<int:pk>/', views.detail_buku, name='detail_buku'),
    path('buku/<int:pk>/reservasi/', views.proses_reservasi, name='reservasi_buku'),
    path('tentang/', views.tentang, name='tentang'),
]