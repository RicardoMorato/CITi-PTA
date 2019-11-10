from django.db import models


class ImagemPerfil(models.Model):

    url = models.URLField('link', max_length=300)

    imagem = models.ImageField('imagem', upload_to='imagens/', null=True, blank=True)
    # Criei uma nova pasta chamada imagens para que o upload seja feito para essa pasta.

    def __str__(self):
        return self.url



class Pessoal(models.Model):

    idade = models.IntegerField('idade')
    # Deixei a idade editável pois ela muda todos os anos, não botei um máximo/mínimo pq o models não é lugar de lógica, posso fazer isso no futuro usando JS.

    namora = models.BooleanField('namoro', default=True)
    # Deixei esse campo como editável só pra ele não ser o diferentão, mas setei o default dele como true, pq espero que ele continue sempre assim kkkkkkk.

    entrar_CITi = models.CharField('citi', max_length=75, blank=True, null=True)
    # Aqui vou botar uma mensagem sobre como está meu ânimo sobre o CITi, editável pois posso ficar mudando a mensagem co o passar do tempo.


    def __str__(self):
        return self.idade


class Hobby(models.Model):
    atividade = models.CharField(max_length=100)
    # O admin pode editar meus hobbys, pois posso mudar de hobbys com o passar do tempo

    def __str__(self):
        return self.atividade


class CoisasQueNaoSouBom(models.Model):
    atividade = models.CharField(max_length=150)

    def __str__(self):
        return self.atividade