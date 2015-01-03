# -*- coding: utf-8 -*-
from peewee import *
from models.shared import BaseModel, Category

class KickerPost(BaseModel):
    '''Post scraped from Kicker microblog'''
    id = IntegerField(primary_key=True)  # id will be get from post id so autoincrementation is undesirable
    title = CharField(max_length=100, null=True)
    description = TextField(null=True)
    url = CharField(null=True)
    popularity = IntegerField(default=0)  # count of 'wykopy'
    image_url = CharField(null=True)
    date = DateTimeField(null=True)
    use_count = IntegerField(default=0)  # how many times post was already publicated on web
    def __str__(self):
        return 'KickerPost id={0}'.format(self.id)
    class Meta:
        db_table = 'kicker_post'

class KickerPostToCategory(BaseModel):
    '''Many-To-Many relation between KickerPost and Category'''
    post = ForeignKeyField(KickerPost)
    category = ForeignKeyField(Category)
    def __str__(self):
        return 'KickerPostToCategory id={0}'.format(self.id)
    class Meta:
        indexes = ((('post', 'category'), True),)
        db_table = 'kicker_post_to_category'