# Generated by Django 4.1.7 on 2023-05-27 10:51

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('is_with_discount', models.BooleanField(default=False)),
                ('default_discount', models.FloatField(validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
            ],
        ),
    ]
