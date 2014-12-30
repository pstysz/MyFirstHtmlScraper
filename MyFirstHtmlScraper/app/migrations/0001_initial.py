# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('url', models.URLField(null=True, blank=True)),
                ('popularity', models.IntegerField(null=True, blank=True)),
                ('image_url', models.URLField(null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('category', models.ManyToManyField(to='app.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
