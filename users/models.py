from django.contrib.auth.models import AbstractUser
from django.db import models

import constants


# Create your models here.


class User(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', **constants.NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __repr__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
