from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    """Modelo para representar los libros de la Biblia"""
    num = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(66)],
        help_text="Número del libro (1-66)"
    )
    name = models.CharField(
        max_length=50,
        help_text="Nombre del libro"
    )
    hebreo = models.CharField(
        max_length=50, 
        blank=True,
        help_text="Nombre en hebreo"
    )
    fonetica = models.CharField(
        max_length=50, 
        blank=True,
        help_text="Transcripción fonética"
    )
    
    class Meta:
        ordering = ["num"]
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return f"{self.num}. {self.name}"

class Bible(models.Model):
    """Modelo para representar las diferentes versiones bíblicas"""
    name = models.CharField(
        max_length=50,
        help_text="Nombre interno del archivo"
    )
    label = models.CharField(
        max_length=50, 
        blank=True,
        help_text="Nombre para mostrar"
    )
    description = models.CharField(
        max_length=100, 
        blank=True,
        help_text="Descripción de la versión"
    )
    file = models.CharField(
        max_length=50,
        help_text="Nombre del archivo .bbli/.bblx"
    )
    visible = models.BooleanField(
        default=True,
        help_text="¿Es visible en la interfaz?"
    )
    activo = models.BooleanField(
        default=False,
        help_text="¿Está activa para mostrar en paralelo?"
    )
    
    class Meta:
        verbose_name = "Biblia"
        verbose_name_plural = "Biblias"
        ordering = ['label']

    def __str__(self):
        return self.label or self.name
    
    def get_file_path(self):
        """Retorna la ruta completa del archivo bíblico"""
        from django.conf import settings
        import os
        return os.path.join(settings.BASE_DIR, 'home', 'bibles', self.file)
    
    def is_file_exists(self):
        """Verifica si el archivo bíblico existe"""
        import os
        return os.path.exists(self.get_file_path())
    