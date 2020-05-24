from django.db import models

# Create your models here.
class Book(models.Model):
    num         = models.IntegerField()
    name        = models.CharField(max_length=50)
    hebreo      = models.CharField(max_length=50, blank=True)
    fonetica    = models.CharField(max_length=50, blank=True)
    
    class Meta:
        ordering = ["num"]

    def __str__(self):
        return self.name

class Bible(models.Model):
    name        =   models.CharField(max_length=50)
    label       =   models.CharField(max_length=50, blank=True)
    description =   models.CharField(max_length=100, blank=True)
    file        =   models.CharField(max_length=50)
    visible     =   models.BooleanField()
    activo      =   models.BooleanField()
    