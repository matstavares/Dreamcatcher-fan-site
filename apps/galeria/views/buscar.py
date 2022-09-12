from galeria.models import Foto
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.db.models import Q


def busca(request):
    lista_fotos = Foto.objects.order_by('data_foto').filter(
        Q(publicada=True) | Q(pessoa=request.user.id))

    if 'buscar' in request.GET:
        titulo_a_buscar = request.GET['buscar']
        lista_fotos = lista_fotos.filter(
            Q(descricao__icontains=titulo_a_buscar)
            | Q(titulo_foto__icontains=titulo_a_buscar))

    dados = {'galeria': lista_fotos}

    return render(request, 'galeria/buscar.html', dados)
