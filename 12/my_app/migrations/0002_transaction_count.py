# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]