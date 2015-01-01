# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150101_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='appears_on_digger',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='appears_on_wp',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
