from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models

from carworld.accounts.managers import CarworldUserManager


class CarworldUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = CarworldUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        CarworldUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
