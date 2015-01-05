# -*- coding: utf-8 -*-
from configuration.settings import DB_HANDLER
from peewee import *
from models.shared import (BaseModel, CategoryGroup, Category, SourceArticle, Content, CATEGORY_GROUP,
                           SourceArticleToCategory, CreatedArticle, CreatedArticleToCategory)
from models.digger import (KickerPost, KickerPostToCategory)

models_to_create = []

# many-to-many models need to be add after other models
models_to_create.append(KickerPost)
models_to_create.append(CategoryGroup)
models_to_create.append(Category)
models_to_create.append(SourceArticle)
models_to_create.append(Content)
models_to_create.append(CreatedArticle)

models_to_create.append(KickerPostToCategory)
models_to_create.append(SourceArticleToCategory)
models_to_create.append(CreatedArticleToCategory)

def __populate_db():
    '''Populate database with prepared data after create new tables'''

    # Populate category_group table
    if not CategoryGroup.select().exists():
        data_to_bulkinsert = []
        for key, elem in CATEGORY_GROUP.items():
            data_to_bulkinsert.append({'id': elem, 'name': key})
        with DB_HANDLER.transaction():
            CategoryGroup.insert_many(data_to_bulkinsert).execute()


def initiate_db():
    '''Connects to specified in configuration database and create tables if necessary'''
    DB_HANDLER.connect()
    DB_HANDLER.create_tables(models_to_create, True)
    __populate_db()