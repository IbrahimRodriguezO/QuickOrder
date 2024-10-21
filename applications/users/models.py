from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(verbose_name="Nombre", max_length=60)
    last_name = models.CharField(verbose_name="Apellido paterno", max_length=40)
    last_name_2 = models.CharField(verbose_name="Apellido materno", max_length=40)

    ROLE_CHOICES = [
        ('owner', 'Dueño'),
        ('waiter', 'Mesero'),
        ('chef', 'Cocinero'),
    ]

    rol = models.CharField(verbose_name="Rol", max_length=20, choices=ROLE_CHOICES)

    username = models.CharField(verbose_name="Usuario", max_length=40, unique=True, default='default_username')
    email = models.EmailField(verbose_name="Email", unique=True)
    password = models.CharField(verbose_name="Contraseña", max_length=100)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de teléfono debe tener el formato: '+999999999'. Hasta 10 dígitos permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Teléfono")

    created_at = models.DateTimeField(verbose_name="Fecha creación", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Fecha de actualización", auto_now=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return f'{self.name} {self.last_name} ({self.email})'