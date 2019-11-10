from django.db import models

# Model responsável por armazenar minhas informações pessoais.
class Pessoal(models.Model):

    idade = models.IntegerField('idade')
    # Deixei a idade editável pois ela muda todos os anos, não botei um máximo/mínimo pq o models não é lugar de lógica, posso fazer isso no futuro usando JS.

    namora = models.BooleanField('namoro', default=True)
    # Deixei esse campo como editável só pra ele não ser o diferentão, mas setei o default dele como true, pq espero que ele continue sempre assim kkkkkkk.

    entrar_CITi = models.CharField("citi", max_length=75, blank=True, null=True)
    # Aqui vou botar uma mensagem sobre como está meu ânimo sobre o CITi, editável pois posso ficar mudando a mensagem co o passar do tempo.


    def __str__(self):
        return self.idade