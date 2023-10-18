from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class Profile(AbstractUser):
    email = models.EmailField(unique=True,null=True,blank=True)
    user_email = models.EmailField(default=None, null=True, unique=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)
    otp = models.CharField(max_length=6,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return str(self.email)