from django.db import models


class customers(models.Model):
    customer = models.CharField(max_length=255)
    time = models.DateTimeField(max_length=255)
    seller = models.CharField(max_length=255)