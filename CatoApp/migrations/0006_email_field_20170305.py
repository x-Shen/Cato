# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatoApp', '0005_user_null_fields_20170304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
