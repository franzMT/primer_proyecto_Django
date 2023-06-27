from django.db import models

# Create your models here.
#tabla primaria
class Categoria(models.Model):
    
    nombre = models.CharField(max_length=20,null=False)
    
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
class Productos(models.Model):
    nombre = models.CharField(max_length=30,null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
        
    
    