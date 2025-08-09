from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    UM = models.CharField(max_length=10, blank=True, null=True)
    almox_principal_id = models.ForeignKey(
        'Almoxarifado', 
        models.DO_NOTHING,
        db_column='almox_principal_id',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'produto'
        managed = False
        
    def __str__(self):
        return self.descricao
    
    
class Almoxarifado(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField(unique=True)
    
    class Meta:
        db_table = 'almoxarifado'
        managed = False
        
    def __str__(self):
        return self.nome
    
class OrdemServico(models.Model): 
    id = models.AutoField(primary_key=True)    
    descricao = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.IntegerField()

    class Meta:
        db_table = 'ordem_servico'
        managed = False
        
    def __str__(self):
        return f"{self.codigo} - {self.descricao or ''}"
    
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