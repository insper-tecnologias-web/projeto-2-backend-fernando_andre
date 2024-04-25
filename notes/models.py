from django.db import models

class Tag(models.Model):
    titulo = models.CharField(max_length=200)

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id) + '.' + ' ' + str(self.title)

class Fact(models.Model):
    descricao = models.TextField(null=True)
    curtidas = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id) + '.' + ' ' + str(self.descricao)

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    promocao = models.BooleanField(default=False)

class Moeda(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id) + '.' + ' ' + str(self.nome) 