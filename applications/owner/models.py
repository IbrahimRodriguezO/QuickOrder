from django.db import models

# Create your models here.
class Menu(models.Model):

    class Meta:
        verbose_name = 'Menú'
        verbose_name_plural = 'Menús'

    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.CharField(verbose_name="Foto", max_length=100)

    TYPE_CHOICES = [
        ("Platillo", "Platillo"),
        ("Bebida", "Bebida"),
    ]

    tipo = models.CharField(verbose_name="Tipo", max_length=50, choices=TYPE_CHOICES)

    existencia = models.BooleanField(default=True)
    created_at = models.DateTimeField(verbose_name="Fecha creación", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Fecha de actualización", auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"

