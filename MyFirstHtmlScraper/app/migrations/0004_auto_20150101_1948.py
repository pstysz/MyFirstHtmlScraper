# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150101_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='use_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='use_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
