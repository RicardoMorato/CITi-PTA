from django.contrib import admin
from .models import Pessoal, ImagemPerfil, Hobby, CoisasQueNaoSouBom, Entretenimento, ImagensCoisasQueGosto
from solo.admin import SingletonModelAdmin
# Os comandos abaixo servem para habilitar o administrador a registrar os models criados

admin.site.register(Pessoal)

admin.site.register(ImagemPerfil, SingletonModelAdmin)

admin.site.register(Hobby)

admin.site.register(CoisasQueNaoSouBom)

admin.site.register(Entretenimento)

admin.site.register(ImagensCoisasQueGosto)