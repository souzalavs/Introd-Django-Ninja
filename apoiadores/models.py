from django.db import models

class Apoiador(models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.TextField()
    
    def __str__(self):
        return self.nome + ": " + self.mensagem