from django.shortcuts import render
from django.views import generic

from .models import Pessoal, ImagemPerfil


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # AS ASPAS DENTRO DOS COLCHETES TÊM QUE SER SIMPLEEEEEEES!!!!
        context['infos'] = Pessoal.objects.all()
        context['imagemPerfil'] = ImagemPerfil.objects.all()
        return context