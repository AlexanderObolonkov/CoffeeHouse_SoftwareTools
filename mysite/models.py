"""Александр"""
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


class Position(models.Model):
    title: models.CharField = models.CharField(max_length=200)
    url: models.SlugField = models.SlugField()
    description: models.TextField = models.TextField()
    image: models.ImageField = models.ImageField()
    price: models.FloatField = models.FloatField(validators=[MinValueValidator(Decimal('0.01'))])
    is_with_discount: models.BooleanField = models.BooleanField(default=False)
    default_discount: models.FloatField = models.FloatField(validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return self.title
