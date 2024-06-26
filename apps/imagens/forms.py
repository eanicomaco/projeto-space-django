from django import forms
from apps.imagens.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['ativo',]
        labels = {
            'descricao':'Descrição',
            'data_fotografia':'Data',
            'usuario_id':'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs = {
                    'type':'date',
                    'class':'form-control',
                }
            ),
            'usuario_id': forms.Select(attrs={'class':'form-control'}),
        }