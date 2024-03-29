# Generated by Django 2.2 on 2019-09-22 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(default=datetime.datetime(2019, 9, 22, 9, 44, 46, 226991), verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(default=datetime.datetime(2019, 9, 22, 9, 44, 46, 227085), verbose_name='修改时间')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='摘要')),
                ('category', models.ForeignKey(on_delete=False, to='blog.Category', verbose_name='分类')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签')),
            ],
        ),
    ]
