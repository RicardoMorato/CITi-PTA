from django.shortcuts import render
from django.views import generic

from .models import ImagemPerfil, Pessoal, Hobby


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # AS ASPAS DENTRO DOS COLCHETES TÊM QUE SER SIMPLEEEEEEES!!!!
        context["imagemPerfil"] = ImagemPerfil.objects.all()
        context["infos"] = Pessoal.objects.all()
        context["hobbys"] = Hobby.objects.all()
        return context