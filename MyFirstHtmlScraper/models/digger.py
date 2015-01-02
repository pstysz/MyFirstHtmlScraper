from configuration import DBSETTINGS
from peewee import *
from shared import db, tables_to_create

SOURCE_CHOICE = (
    (0, 'Unknown'),
    (1, 'PcLab'),
)

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
    title = CharField(max_length=100, null=True)
    description = TextField(null=True)
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