# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-28 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('search', models.CharField(max_length=256, verbose_name='搜索内容')),
                ('sort', models.CharField(max_length=16, verbose_name='排序依据')),
                ('title', models.CharField(max_length=1024, verbose_name='名称')),
                ('price', models.CharField(max_length=32, verbose_name='价格')),
                ('shop', models.CharField(max_length=32, verbose_name='商店')),
                ('img', models.CharField(max_length=2048, verbose_name='图片')),
            ],
            options={
                'db_table': 'jd',
                'verbose_name_plural': '京东',
                'verbose_name': '京东',
            },
        ),
    ]
