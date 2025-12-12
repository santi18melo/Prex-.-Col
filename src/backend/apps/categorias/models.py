from django.db import models

class Categoria(models.Model):
    """
    Modelo que representa una categoría de productos.
    Permite organizar los productos de manera jerárquica o simple.
    """
    nombre = models.CharField(max_length=100, unique=True, help_text="Nombre de la categoría")
    slug = models.SlugField(max_length=100, unique=True, help_text="Slug único para URLs de categoría")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción breve de la categoría")
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True, help_text="Imagen representativa de la categoría")
    
    activa = models.BooleanField(default=True, help_text="Indica si la categoría está activa y visible")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
