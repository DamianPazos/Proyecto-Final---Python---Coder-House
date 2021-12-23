from django.db import models

# Create your models here.

# Modelo sobre bebidas 
class Bebidas(models.Model):
    
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=3)
    cantidad = models.DecimalField(max_digits=7,decimal_places=2)
    is_light = models.BooleanField()
    is_alcohol = models.BooleanField()
    sabor = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=7,decimal_places=2)
    
    def __str__(self):
        return f'Bebida marca {self.marca}'
    
    
    # Modelo sobre golosinas
class Golosinas(models.Model):
    
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=3)
    cantidad = models.DecimalField(max_digits=7,decimal_places=2)
    precio = models.DecimalField(max_digits=7,decimal_places=2)
    is_light = models.BooleanField()
    is_free_gluten = models.BooleanField()
    
    
    # Modelo sobre cigarrillos
class Cigarrillos(models.Model):
    
    marca = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=7,decimal_places=2)
    sabor = models.CharField(max_length=15)
