from django.shortcuts import render
from django.views import generic
from .models import Pessoal

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["infos"] = Pessoal.objects.all()
        return context