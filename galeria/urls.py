from django.urls import path
from galeria.views import index, imagem
# from galeria.views import imagem --> pode ser feito de forma simplificada, conf. acima

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]
