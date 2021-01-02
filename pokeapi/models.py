from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    height = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)


