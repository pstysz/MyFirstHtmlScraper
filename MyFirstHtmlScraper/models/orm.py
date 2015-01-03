# -*- coding: utf-8 -*-
from configuration.settings import DB_HANDLER
from peewee import *
from models.shared import BaseModel, Category, SourceArticle, Content, SourceArticleToCategory
from models.digger import KickerPost, KickerPostToCategory

models_to_create = []

# many-to-many models need to be add after other models
models_to_create.append(KickerPost)
models_to_create.append(Category)
models_to_create.append(SourceArticle)
models_to_create.append(Content)

models_to_create.append(KickerPostToCategory)
models_to_create.append(SourceArticleToCategory)

def initiate_db():
    '''Connects to specified in configuration database and create tables if necessary'''
    DB_HANDLER.connect()
    DB_HANDLER.create_tables(models_to_create, True)