from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de categoria')
    
    def __str__(self):
        return self.nombreCategoria

class Libro(models.Model):
    ISBN = models.IntegerField(primary_key=True, verbose_name='Id de libro')
    nombreLibro = models.CharField(max_length=50, verbose_name='Nombre de libro')
    autor = models.CharField(max_length=50, verbose_name='Nombre del autor')
    Descripcion = models.CharField(max_length=100, verbose_name='Descripcion del libro')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreLibro