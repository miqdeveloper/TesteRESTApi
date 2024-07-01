from django.db import models


class Venda(models.Model):
    
    produto_Id = models.IntegerField(auto_created=True, unique=True)
    name = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco  = models.IntegerField()
    mtd_pg = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
class Vendedor(models.Model):
    
    name = models.CharField(max_length=50)
    cnpj = models.IntegerField()
    
    def __str__(self):
        return self.name


    
class Comprador(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nomeVendedor