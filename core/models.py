from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=255)
    nivel_acesso = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'usuario'
        managed = False #Nao deixa o Django controlar a tabela
        
    def __str__(self):
        return self.nome