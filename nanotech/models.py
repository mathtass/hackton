
from django.conf import settings
from django.db import models
from django.utils import timezone



class Login(models.Model):
    nome = models.CharField(max_length=200,null=False)
    cpf = models.IntegerField(null=False)
    endereco = models.CharField(max_length=200,null=False)
    email = models.EmailField(null=False)
    celular = models.IntegerField(null=False)
    telefone = models.IntegerField(null=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Formulario(models.Model):
    usuario = models.ForeignKey(Login,null=False, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=200,null=False)
    descricao = models.CharField(max_length=200,null=False)
    data = models.DateTimeField(default=timezone.now)
    numero = models.IntegerField(null=False)
    numero_reclamacao = models.IntegerField(null=False)
    status = models.CharField(max_length=200,null=False)
    anexo = models.FileField(upload_to="\nanotech")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
