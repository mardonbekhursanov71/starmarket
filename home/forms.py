from django import forms
from .models import Mahsulot

class MahsulotForm(forms.ModelForm):
    class Meta:
        model = Mahsulot
        fields = ['nomi', 'narxi', 'turi', 'qoshimcha_malumot']
        widgets = {
            'image': forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'})),
            'nomi': forms.TextInput(attrs={'class': 'form-control'}),
            'narxi': forms.NumberInput(attrs={'class': 'form-control'}),
            'turi': forms.Select(attrs={'class': 'form-select'}),
            'qoshimcha_malumot': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
