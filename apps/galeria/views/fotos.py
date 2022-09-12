from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from galeria.models import Foto
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from galeria.forms import FotoForm


def index(request):
    fotos = Foto.objects.order_by('-data_foto').filter(publicada=True)
    dados = {'galeria': fotos}

    foto = FotoForm()
    contexto = {'form': foto}

    return render(request, 'galeria/index.html', dados)


def foto(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    form = FotoForm(instance=foto)
    foto_a_exibir = {'foto': form}

    return render(request, 'galeria/galeria.html', foto_a_exibir)


def cria_foto(request):
    if request.method == 'POST':
        titulo_foto = request.POST['titulo_foto']
        descricao = request.POST.get('descricao', '')
        fonte = request.POST.get('fonte', '')
        votos = request.POST.get('votos', 0)
        if votos == '':
            votos = 0
        local = request.POST.get('local', '')
        categoria = request.POST['categoria']
        data_foto = request.POST['data_foto']
        if data_foto == '':
            data_foto = None
        publicada = request.POST.get('publicada', False) == 'on'
        fotinha = request.FILES['fotinha']
        user = get_object_or_404(User, pk=request.user.id)
        foto = Foto.objects.create(pessoa=user,
                                   titulo_foto=titulo_foto,
                                   descricao=descricao,
                                   fonte=fonte,
                                   votos=votos,
                                   local=local,
                                   categoria=categoria,
                                   data_foto=data_foto,
                                   publicada=publicada,
                                   fotinha=fotinha)
        foto.save()
        return redirect('dashboard')
    else:
        return render(request, 'galeria/cria_foto.html')


def deleta_foto(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    foto.delete()
    return redirect('dashboard')


def edita_foto(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    form = FotoForm(instance=foto)
    foto_a_editar = {'form': form, 'id': foto_id}

    return render(request, 'galeria/edita_foto.html', foto_a_editar)


def atualiza_foto(request, foto_id):
    if request.method == 'POST':
        f = Foto.objects.get(pk=foto_id)
        f.titulo_foto = request.POST['titulo_foto']
        f.descricao = request.POST.get('descricao', '')
        f.fonte = request.POST.get('fonte', '')
        f.votos = request.POST.get('votos', 0)
        f.local = request.POST.get('local', '')
        f.categoria = request.POST['categoria']
        f.data_foto = request.POST['data_foto']
        if f.data_foto == '':
            f.data_foto = None
        f.publicada = request.POST.get('publicada', False) == "on"
        if 'fotinha' in request.FILES:
            f.fotinha = request.FILES['fotinha']
        f.save()
    return redirect('dashboard')
