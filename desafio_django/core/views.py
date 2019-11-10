from django.shortcuts import render
from django.views import generic

from .models import ImagemPerfil, Pessoal, Hobby, CoisasQueNaoSouBom, Entretenimento, ImagensCoisasQueGosto


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context["imagemPerfil"] = ImagemPerfil.objects.all()
        context["infos"] = Pessoal.objects.all()
        context["hobbys"] = Hobby.objects.all()
        context["coisas_que_nao_sou_bom"] = CoisasQueNaoSouBom.objects.all()
        context["obras_de_entretenimento"] = Entretenimento.objects.all()
        context["imagens_coisas_que_gosto"] = ImagensCoisasQueGosto.objects.all()
        return context