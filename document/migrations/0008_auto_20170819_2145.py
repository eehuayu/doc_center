# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-19 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0007_auto_20170819_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='my_file',
            field=models.FileField(upload_to='/upload', verbose_name='文件'),
        ),
    ]
