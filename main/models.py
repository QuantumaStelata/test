from django.db import models

# Create your models here.


class Term(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name
