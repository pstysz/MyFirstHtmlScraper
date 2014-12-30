# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.PositiveIntegerField(primary_key=True) #id will be get from post id so autoincrementation is undesirable
    title = models .CharField(max_length=100)
    description = models.TextField(max_length=500)
    url = models.URLField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True) # count of 'wykopy'
    image_url = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title