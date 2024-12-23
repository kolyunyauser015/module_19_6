from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Buyer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title
