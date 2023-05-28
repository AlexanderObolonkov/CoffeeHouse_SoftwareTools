# mypy: ignore-errors
from decimal import Decimal

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Position(models.Model):
    title = models.CharField(max_length=200)
    url = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField(validators=[MinValueValidator(Decimal('0.01'))])
    is_with_discount = models.BooleanField(default=False)
    default_discount = models.FloatField(validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return self.title


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    birth_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.SlugField()
    description = models.TextField()
    content = RichTextUploadingField()
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
