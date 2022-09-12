from django.urls import path

from .views.buscar import *
from .views.fotos import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:foto_id>', foto, name='foto'),
    path('buscar', busca, name='buscar'),
    path('cria/fotos', cria_foto, name='cria_foto'),
    path('deleta/<int:foto_id>', deleta_foto, name='deleta_foto'),
    path('edita/<int:foto_id>', edita_foto, name='edita_foto'),
    path('atualiza_foto/<int:foto_id>', atualiza_foto, name='atualiza_foto')
]
