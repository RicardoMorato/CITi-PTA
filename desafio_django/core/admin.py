from django.contrib import admin
from .models import Pessoal
from .models import ImagemPerfil
from .models import Hobby
from .models import CoisasQueNaoSouBom

# Register your models here.

admin.site.register(Pessoal)
# Cria a opção do administrador editar o modelo 'Pessoal'.

admin.site.register(ImagemPerfil)
# Cria a opcao do administrador de editar a imagem de perfil

admin.site.register(Hobby)
# Cria a opcao do administrador de editar os hobbys.

admin.site.register(CoisasQueNaoSouBom)
# Cria essa nova opcao de registro também.