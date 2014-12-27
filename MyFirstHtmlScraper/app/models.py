from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    id = models.PositiveIntegerField(primary_key=True) #id will be get from post id so autoincrementation is undesirable
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    url = models.URLField()
    popularity = models.IntegerField() # count of 'wykopy'
    image_url = models.URLField()
    date = models.DateField()
    category = models.ManyToManyField(Category)