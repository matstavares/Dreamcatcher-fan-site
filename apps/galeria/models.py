from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Foto(models.Model):
    '''modelo'''
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_foto = models.CharField(max_length=200, blank=True)
    descricao = models.TextField(default='', blank=True, max_length=200)
    fonte = models.CharField(default='', blank=True, max_length=200)
    votos = models.IntegerField(default=0)
    local = models.CharField(default='', max_length=200, blank=True)
    categoria = models.CharField(default='', max_length=200, blank=True)
    data_foto = models.DateField(default=datetime.now, blank=True, null=True)
    fotinha = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.titulo_foto
