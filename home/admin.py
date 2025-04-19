from django.contrib import admin
from .models import Mahsulot

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ['image', 'nomi', 'narxi', 'turi', 'qisqa_izoh']
    list_filter = ['turi']
    search_fields = ['nomi', 'qoshimcha_malumot']
    ordering = ['nomi']

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            'fields': ('nomi', 'narxi', 'turi')
        }),
        ("Qo‘shimcha", {
            'fields': ('qoshimcha_malumot',),
            'classes': ('collapse',),
        }),
    )

    def qisqa_izoh(self, obj):
        return (obj.qoshimcha_malumot[:40] + '...') if obj.qoshimcha_malumot else "-"
    qisqa_izoh.short_description = "Izoh"
