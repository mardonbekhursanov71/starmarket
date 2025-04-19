from django.db import models

class Mahsulot(models.Model):
    TUR_CHOICES = [
        ('oz', 'Oziq-ovqat'),
        ('kiyim', 'Kiyim-kechak'),
        ('elek', 'Elektronika'),
        ('boshqa', 'Boshqa'),
    ]
    image = models.ImageField(upload_to='staticfiles/img', null=True, blank=True)
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    turi = models.CharField(max_length=10, choices=TUR_CHOICES)
    qoshimcha_malumot = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nomi} - {self.get_turi_display()} - {self.narxi} so'm"