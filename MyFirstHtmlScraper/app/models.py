# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    popularity = models.IntegerField(default=0) # how often category appears in posts
    is_disabled = models.BooleanField(default=False) # admin can disable some unwanted categories

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'app'

class Post(models.Model):
    id = models.PositiveIntegerField(primary_key=True) #id will be get from post id so autoincrementation is undesirable
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    url = models.URLField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True) # count of 'wykopy'
    image_url = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'

class Content(models.Model):
    text = models.TextField()
    text_length = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        self.text_length = len(self.text)
        super(ModelClass, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'