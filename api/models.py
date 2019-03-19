from django.db import models


class Token(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=50)
    icon = models.TextField()
