# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_category', '0005_category_reindex_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title', 'pk'], 'verbose_name': 'subject', 'verbose_name_plural': 'subjects'},
        ),
    ]
