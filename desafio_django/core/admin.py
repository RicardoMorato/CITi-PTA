from django.contrib import admin
from .models import Pessoal
from .models import ImagemPerfil

# Register your models here.

admin.site.register(Pessoal)
# Cria a opção do administrador editar o modelo 'Pessoal'.

admin.site.register(ImagemPerfil)
# Cria a opcao do administrador de editar a imagem de perfil