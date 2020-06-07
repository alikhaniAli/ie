from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


class Product(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('name', max_length=50)
    company_name = models.CharField('Company name', max_length=40)
    pro_date = models.DateTimeField('pro date', auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)

    objects = UserManager()

    REQUIRED_FIELDS = []