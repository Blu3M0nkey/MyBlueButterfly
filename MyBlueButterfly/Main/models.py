"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
# Create your models here.
# will create DB tables from classes..
# 


class recipie (models.Model):
    name = models.CharField(max_length = 100)
    ingredents = models.TextField()
    directions = models.TextField()

    def __str__(self):
        return self.title




 