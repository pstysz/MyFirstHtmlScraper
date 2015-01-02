# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150102_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_extracted', models.BooleanField(default=False)),
                ('source', models.IntegerField(default=0, choices=[(0, 'Unknown'), (1, 'PcLab')])),
                ('category', models.ManyToManyField(to='app.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
