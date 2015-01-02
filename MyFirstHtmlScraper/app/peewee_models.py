import configuration
from peewee import *


db = SqliteDatabase(**configuration.DBSETTINGS['sqlite'])

class BaseModel(Model):
    class Meta:
        database = db





def create_tables():
    db.connect()
    db.create_tables([Post, Category], True)

# -------------------------------------------------------------


SOURCE_CHOICE = (
    (0, 'Unknown'),
    (1, 'PcLab'),
)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    popularity = models.IntegerField(default=0) # how often category appears in posts
    is_disabled = models.BooleanField(default=False) # admin can disable some unwanted categories
    appears_on_digger = models.BooleanField(default=False) # does this category appear on digger?
    appears_on_wp = models.BooleanField(default=False) # does this category appear on WP?
    #TODO: Think about split popularity depending on source
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
    use_count = models.IntegerField(default=0) # how many times this post was publicated on web
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'

class Content(models.Model):
    text = models.TextField()
    text_length = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    use_count = models.IntegerField(default=0) # how many times this text was already publicated on web
    source = models.IntegerField(default=0, choices=SOURCE_CHOICE)
    source_id = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        self.text_length = len(self.text)
        super(ModelClass, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'

class SourceArticle(models.Model):
    '''Article to extract content'''
    text = models.TextField()
    category = models.ManyToManyField(Category)
    is_extracted = models.BooleanField(default=False)
    source = models.IntegerField(default=0, choices=SOURCE_CHOICE)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'