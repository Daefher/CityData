from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    population = models.IntegerField(default=0)
    area = models.FloatField(default=0.0)
    top_attractions = models.TextField(blank=True, null=True)  # or JSONField if using Django 3.1+
    latitude = models.CharField(max_length=255,null=True)
    longitude = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    summary  = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.name