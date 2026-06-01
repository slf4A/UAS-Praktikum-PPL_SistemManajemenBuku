from django import forms
from .models import Reservasi

class ReservasiForm(forms.ModelForm):
    class Meta:
        model = Reservasi
        fields = ['nama_peminjam', 'email_peminjam']
        widgets = {
            'nama_peminjam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama Anda'}),
            'email_peminjam': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Email Anda'}),
        }