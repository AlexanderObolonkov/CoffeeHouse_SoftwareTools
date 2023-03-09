# Generated by Django 4.1.7 on 2023-03-09 16:09

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='default_discount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
