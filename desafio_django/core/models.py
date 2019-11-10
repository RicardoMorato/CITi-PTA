from django.db import models

# Model responsável por armazenar minhas informações pessoais.
class Pessoal(models.Model):
    nome = models.CharField('Nome', max_length=100)
    # Aqui estou dando um tamanho máximo para o nome, deixei o nome deitável pq é algo editável na vida real.

    idade = models.IntegerField('Idade')
    # Deixei a idade editável pois ela muda todos os anos, não botei um máximo/mínimo pq o models não é lugar de lógica, posso fazer isso no futuro usando JS.

    namora = models.BooleanField('Namoro', default=True)
    # Deixei esse campo como editável só pra ele não ser o diferentão, mas setei o default dele como true, pq espero que ele continue sempre assim kkkkkkk.

    entrar_CITi = models.CharField("CITi", max_length=30, blank=True, null=True)
    # Aqui vou botar uma mensagem sobre como está meu ânimo sobre o CITi, editável pois posso ficar mudando a mensagem co o passar do tempo.


    def __str__(self):
        return self.nome