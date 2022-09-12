from django.contrib import admin
from .models import Foto


class ListandoFotos(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo_foto',
        'categoria',
        'votos',
        'publicada',
    ]
    list_editable = [
        'categoria',
        'votos',
        'publicada',
    ]

    list_display_links = [
        'id',
        'titulo_foto',
    ]
    search_fields = ['titulo_foto']
    list_filter = ['categoria']
    #list_per_page = 5


admin.site.register(Foto, ListandoFotos)
