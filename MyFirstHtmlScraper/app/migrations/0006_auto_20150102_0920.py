# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150101_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='source',
            field=models.IntegerField(default=0, choices=[(0, 'Unknown'), (1, 'PcLab')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='source_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
