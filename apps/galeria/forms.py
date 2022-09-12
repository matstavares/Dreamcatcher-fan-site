from datetime import date
from socket import fromshare
from django import forms
from galeria.models import Foto


class FotoForm(forms.ModelForm):

    class Meta:
        model = Foto
        fields = '__all__'
        labels = {
            'titulo_foto': 'Título',
            'descricao': 'Descrição',
            "data_foto": "Data"
        }
        # widgets = {
        #     'date': forms.DateInput(attrs={'class': 'datepicker'}),
        # }

    # titulo_foto = forms.CharField(label="Título", max_length=200)
    # publicada = forms.BooleanField(label="Publicar?")
    # descricao = forms.CharField(label="Descrição")
    # fonte = forms.CharField(label="Fonte")
    # votos = forms.DecimalField(label="Votos")
    # local = forms.CharField(label="Local")
    # categoria = forms.CharField(label="Categoria")
    # data_foto = forms.DateField(label="Data")
    # # fotinha = forms.FilePathField(label="Caminho", path='fotos/%d/%m/%Y/')
    # pessoa = forms.DecimalField(label="Usuário")
