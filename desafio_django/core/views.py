from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.core.mail import EmailMessage
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



def index(request):
    return render(request, 'home.html')


def email(request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    assunto = request.POST.get('subject')
    mensagem = request.POST.get('message')


    subject = assunto
    body = f'Nome: {nome}\nAssunto: {assunto}\nEmail: {email}\nMensagem: {mensagem}'

    mail  = EmailMessage(subject, body, 'desafioPTAdjangoCITi2019.2@gmail.com', ['desafioPTAdjangoCITi2019.2@gmail.com', 'rmr@cin.ufpe.br'])
    result = mail.send()
    return HttpResponse(status=201)