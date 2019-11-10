from django.db import models


class ImagemPerfil(models.Model):

    url = models.URLField('link', max_length=300)

    imagem = models.ImageField('imagem', upload_to='imagens/', null=True, blank=True)
    # Criei uma nova pasta chamada imagens para que o upload seja feito para essa pasta.

    class Meta:
        verbose_name = 'Imagem de Perfil'
        verbose_name_plural = 'Imagens de Perfil'

    def __str__(self):
        return self.url



class Pessoal(models.Model):

    idade = models.IntegerField('idade')
    # Deixei a idade editável pois ela muda todos os anos, não botei um máximo/mínimo pq o models não é lugar de lógica, posso fazer isso no futuro usando JS.

    namora = models.BooleanField('namoro', default=True)
    # Deixei esse campo como editável só pra ele não ser o diferentão, mas setei o default dele como true, pq espero que ele continue sempre assim kkkkkkk.

    entrar_CITi = models.CharField('citi', max_length=75, blank=True, null=True)
    # Aqui vou botar uma mensagem sobre como está meu ânimo sobre o CITi, editável pois posso ficar mudando a mensagem co o passar do tempo.

    class Meta:
        verbose_name = 'Informação pessoal'
        verbose_name_plural = 'Informações pessoais'

    def __str__(self):
        return self.idade


class Hobby(models.Model):
    atividade = models.CharField(max_length=100)
    # O admin pode editar meus hobbys, pois posso mudar de hobbys com o passar do tempo

    def __str__(self):
        return self.atividade


class CoisasQueNaoSouBom(models.Model):
    atividade = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Atividade que posso melhorar'
        verbose_name_plural = 'Atividades que posso melhorar'

    def __str__(self):
        return self.atividade

class Entretenimento(models.Model):
    nome_da_obra = models.CharField('nome', max_length=200)
    url_sobre_a_obra = models.URLField('link', max_length=400, null=True, blank=True)

    class Meta:
        verbose_name = 'Obra de entretenimento'
        verbose_name_plural = 'Obras de entretenimento'

    def __str__(self):
        return self.nome_da_obra