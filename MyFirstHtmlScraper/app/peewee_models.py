from configuration import DBSETTINGS
from peewee import *

db = SqliteDatabase(**DBSETTINGS['sqlite3'])

SOURCE_CHOICE = (
    (0, 'Unknown'),
    (1, 'PcLab'),
)

tables_to_create = []

class BaseModel(Model):
    '''Abstract class used to set parameters for every model'''
    class Meta:
        database = db
tables_to_create.append(BaseModel)

class Category(BaseModel):
    '''Categories binded to posts, content and articles'''
    name = CharField(max_length=50, unique=True)
    popularity_kicker = IntegerField(default=0)  # how often category appears on kicker site
    popularity_pclab = IntegerField(default=0)  # how often category appears on pclab site
    is_disabled = BooleanField(default=False)
    def __str__(self):
        return self.name
tables_to_create.append(Category)

class KickerPost(BaseModel):
    '''Post scraped from Kicker microblog'''
    id = IntegerField(primary_key=True)  # id will be get from post id so autoincrementation is undesirable
    title = CharField(max_length=100)
    description = TextField()
    url = CharField(null=True)
    popularity = IntegerField(default=0)  # count of 'wykopy'
    image_url = CharField(null=True)
    date = DateTimeField(null=True)
    use_count = IntegerField(default=0)  # how many times post was already publicated on web
    def __str__(self):
        return self.title
tables_to_create.append(KickerPost)

class KickerPostToCategory(BaseModel):
    '''Many-To-Many relation between KickerPost and Category'''
    post = ForeignKeyField(KickerPost)
    category = ForeignKeyField(Category)
    class Meta:
        indexes = ((('post', 'category'), True),)
tables_to_create.append(KickerPostToCategory)

class SourceArticle(Model):
    '''Article to extract content'''
    text = TextField()
    is_extracted = BooleanField(default=False)  # is content already extracted from article
    source = IntegerField(default=0, choices=SOURCE_CHOICE)
    source_id = IntegerField(null=True)
    def __str__(self):
        return self.text
    class Meta:
        indexes = ((('source', 'source_id'), True),)
tables_to_create.append(SourceArticle)

class SourceArticleToCategory(BaseModel):
    '''Many-To-Many relation between SourceArticle and Categories'''
    source_article = ForeignKeyField(SourceArticle)
    category = ForeignKeyField(Category)
    class Meta:
        indexes = ((('source_article', 'category'), True),)
tables_to_create.append(SourceArticleToCategory)

class Content(BaseModel):
    '''Part of text, scraped from bigger article'''
    text = TextField()
    text_length = IntegerField(default=0)  # strored on db to avoid calling len() before getting text value each time
    use_count = IntegerField(default=0)  # how many times this text was already publicated on web
    article = ForeignKeyField(SourceArticle)
    def __str__(self):
        return self.text
    def save(self, *args, **kwargs):
        self.text_length = len(self.text)
        return super(Blog, self).save(*args, **kwargs)
tables_to_create.append(Content)


def initiate_db():
    '''Connects to specified in configuration database and create tables if necessary'''
    db.connect()
    db.create_tables(tables_to_create, True)