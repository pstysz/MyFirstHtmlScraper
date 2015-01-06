# -*- coding: utf-8 -*-
from peewee import *
from configuration.settings import DB_HANDLER

SOURCE_TYPE = {
    'unknown': 0,
    'pclab': 1,
    'pcworld': 2,
    'komputerswiat': 3,
    'di': 4, #http://di.com.pl/ 
    'frazpc': 5
}

CATEGORY_GROUP = {
    'unknown': 0,
    'motorization': 1,
    'it': 2,
    'business': 3,
    'humour': 4
}

class BaseModel(Model):
    '''Abstract class used to set parameters for every model'''
    class Meta:
        database = DB_HANDLER

class CategoryGroup(BaseModel):
    '''Thematic group of category'''
    id = IntegerField(primary_key=True)
    name = CharField(max_length=50, unique=True)
    is_disabled = BooleanField(default=False)
    def __str__(self):
        return 'CategoryGroup id={0}'.format(self.id)
    class Meta:
        db_table = 'category_group'

class Category(BaseModel):
    '''Categories binded to posts, content and articles'''
    name = CharField(max_length=50, unique=True)
    popularity_kicker = IntegerField(default=0)  # how often category appears on kicker site
    popularity_pclab = IntegerField(default=0)  # how often category appears on pclab site
    is_disabled = BooleanField(default=False)
    category_group = ForeignKeyField(CategoryGroup, default=0)
    def __str__(self):
        return 'Category id={0}'.format(self.id)

class SourceArticle(BaseModel):
    '''Article to extract content'''
    text = TextField()
    is_extracted = BooleanField(default=False)  # is content already extracted from article
    source_type = IntegerField(default=0)  # value from SOURCE_TYPE dictionary
    source_id = IntegerField(default=0)
    def __str__(self):
        return 'SourceArticle id={0}'.format(self.id)
    class Meta:
        indexes = ((('source_type', 'source_id'), True),)
        db_table = 'source_article'

class SourceArticleToCategory(BaseModel):
    '''Many-To-Many relation between SourceArticle and Categories'''
    source_article = ForeignKeyField(SourceArticle)
    category = ForeignKeyField(Category)
    def __str__(self):
        return 'SourceArticleToCategory id={0}'.format(self.id)
    class Meta:
        indexes = ((('source_article', 'category'), True),)
        db_table = 'source_article_to_category'

class Content(BaseModel):
    '''Part of text, scraped from bigger article'''
    text = TextField()
    text_length = IntegerField(default=0)  # stored on db to avoid calling len() before getting text value each time
    use_count = IntegerField(default=0)  # how many times this text was already published on web
    article = ForeignKeyField(SourceArticle)
    def __str__(self):
        return 'Content id={0}'.format(self.id)
    def save(self, *args, **kwargs):
        self.text_length = len(self.text)
        return super(Content, self).save(*args, **kwargs)

class CreatedArticle(BaseModel):
    '''Article created from extracted content'''
    text = TextField()
    is_published = BooleanField(default=False)  # is already on website
    thumbnail = CharField(null=True)
    def __str__(self):
        return 'CreatedArticle id={0}'.format(self.id)
    class Meta:
        db_table = 'created_article'

class CreatedArticleToCategory(BaseModel):
    '''Many-To-Many relation between CreatedArticle and Categories'''
    created_article = ForeignKeyField(CreatedArticle)
    category = ForeignKeyField(Category)
    def __str__(self):
        return 'CreatedArticleToCategory id={0}'.format(self.id)
    class Meta:
        indexes = ((('created_article', 'category'), True),)
        db_table = 'created_article_to_category'