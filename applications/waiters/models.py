from django.db import models

# Create your models here.
class Orden(models.Model):

    class Meta():
        verbose_name = "Órden"
        verbose_name_plural = "Órdenes"

    id = models.AutoField(primary_key=True)

    mesa = models.CharField("Mesa", max_length=1000)
    platillos = models.CharField("Platillos", max_length=1000)
    completado = models.BooleanField(verbose_name= "Estatus",default=False)
    fecha_pedido = models.DateTimeField(verbose_name="Fecha pedido", auto_now_add=True)

    def __str__(self):
        return f"Mesa: {self.mesa}"