from configuration.configuration import DBSETTINGS
from peewee import *


#class SourceArticle(Model):
#    '''Article to extract content'''
#    text = TextField()
#    is_extracted = BooleanField(default=False)  # is content already extracted from article
#    source = IntegerField(default=0, choices=SOURCE_CHOICE)
#    source_id = IntegerField(null=True)
#    def __str__(self):
#        return self.text
#    class Meta:
#        indexes = ((('source', 'source_id'), True),)
#tables_to_create.append(SourceArticle)

#class SourceArticleToCategory(BaseModel):
#    '''Many-To-Many relation between SourceArticle and Categories'''
#    source_article = ForeignKeyField(SourceArticle)
#    category = ForeignKeyField(Category)
#    class Meta:
#        indexes = ((('source_article', 'category'), True),)
#tables_to_create.append(SourceArticleToCategory)

#class Content(BaseModel):
#    '''Part of text, scraped from bigger article'''
#    text = TextField()
#    text_length = IntegerField(default=0)  # strored on db to avoid calling len() before getting text value each time
#    use_count = IntegerField(default=0)  # how many times this text was already publicated on web
#    article = ForeignKeyField(SourceArticle)
#    def __str__(self):
#        return self.text
#    def save(self, *args, **kwargs):
#        self.text_length = len(self.text)
#        return super(Blog, self).save(*args, **kwargs)
#tables_to_create.append(Content)


def initiate_db():
    '''Connects to specified in configuration database and create tables if necessary'''
    db.connect()
    db.create_tables(tables_to_create, True)