from django.contrib import admin
from .models import Pessoal
from .models import ImagemPerfil
from .models import Hobby
from .models import CoisasQueNaoSouBom
from .models import Entretenimento
from .models import ImagensCoisasQueGosto

# Os comandos abaixo servem para habilitar o administrador a registrar os models criados

admin.site.register(Pessoal)

admin.site.register(ImagemPerfil)

admin.site.register(Hobby)

admin.site.register(CoisasQueNaoSouBom)

admin.site.register(Entretenimento)

admin.site.register(ImagensCoisasQueGosto)