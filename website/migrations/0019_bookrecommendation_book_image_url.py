# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20170422_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrecommendation',
            name='book_image_url',
            field=models.URLField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
