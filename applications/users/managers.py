from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff, is_superuser, rol, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            rol=rol,
            **extra_fields 
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, rol="waiter", **extra_fields):
        if rol not in ['waiter', 'chef']:
            raise ValueError("El rol debe ser 'mesero' o 'cocinero'.")
        return self._create_user(username, email, password, False, False, rol, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, "onwer", **extra_fields)